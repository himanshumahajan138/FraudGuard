import cv2
import numpy as np

def correct_skew(image):
    """
    Corrects skew (tilting) in an image using OpenCV.

    Args:
        image (np.ndarray): The input image as a NumPy array. Can be grayscale or BGR color format.

    Returns:
        tuple: A tuple containing two elements:
            - The corrected (rotated) image as a NumPy array.
            - The estimated skew angle in degrees (float).
    """

    # Handle color conversion if necessary
    if len(image.shape) == 2:
        # Grayscale image detected, convert to BGR for OpenCV compatibility
        color_image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
    else:
        # Color image assumed to be in BGR format (blue, green, red)
        color_image = image

    # Convert the image to grayscale for better skew detection
    gray = cv2.cvtColor(color_image, cv2.COLOR_BGR2GRAY)

    # Apply Otsu's thresholding to create a binary image for edge detection
    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    #   - thresh: The resulting binary image after thresholding.
    #   - cv2.THRESH_BINARY_INV: Inverts the thresholding result (darker pixels to white, lighter to black).
    #   - cv2.THRESH_OTSU: Applies Otsu's method for automatic threshold selection.

    # Calculate projection profile to estimate skew angle
    h, w = thresh.shape  # Get image height and width

    scores = []  # List to store scores for different skew angles
    angles = np.arange(-5, 6, 1)  # Range of angles to search for skew (-5 to +5 degrees in steps of 1)

    for angle in angles:
        # Rotate the thresholded image to analyze projection profile
        rotated = cv2.rotate(thresh, cv2.ROTATE_90_CLOCKWISE, dst=thresh)  # Create a rotated copy to avoid modifying thresh

        # Calculate projection histogram: sum pixel intensities along columns
        hist = np.sum(rotated, axis=1, dtype=float)

        # Calculate projection score based on difference between consecutive histogram elements
        # Higher score indicates potentially better alignment after rotation due to more significant intensity changes.
        score = np.sum((hist[1:] - hist[:-1]) ** 2, dtype=float)
        scores.append(score)

    # Find the angle with the maximum projection profile difference (indicating alignment)
    best_angle = angles[scores.index(max(scores))]

    # Correct image skew by rotating it
    center = (w // 2, h // 2)  # Calculate image center coordinates
    M = cv2.getRotationMatrix2D(center, best_angle, 1.0)  # Create rotation matrix for specified angle
    corrected = cv2.warpAffine(
        image, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE
    )
    #   - cv2.warpAffine: Applies an affine transformation (rotation in this case) to the image.
    #   - flags=cv2.INTER_CUBIC: Interpolation method for resampling pixels during rotation (cubic for smoother results).
    #   - borderMode=cv2.BORDER_REPLICATE: Pixel extrapolation method to handle out-of-image regions (replicates edge pixels).

    return corrected, best_angle


def variance_of_laplacian(image):
    """
    Calculates the variance of the Laplacian of a grayscale image, which is a measure of image sharpness.

    Args:
        image (np.ndarray): The image as a NumPy array.

    Returns:
        float: The variance of the Laplacian.
    """

    # Handle color and grayscale images
    if len(image.shape) == 2:  # Grayscale image
        color_image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)  # Convert to BGR for consistency
    else:  # Color image (assumed to be BGR)
        color_image = image

    # Convert to grayscale if necessary
    gray = cv2.cvtColor(color_image, cv2.COLOR_BGR2GRAY)

    # Calculate the Laplacian and its variance
    laplacian = cv2.Laplacian(gray, cv2.CV_64F)  # Use double-precision for accuracy
    var = laplacian.var()

    return var


def preprocess_image(image_path, apply_binarization=False, blur_threshold=50):
    """
    Preprocesses an image for improved OCR performance.

    Args:
        image_path (str): Path to the image file.
        apply_binarization (bool, optional): Whether to apply binarization (thresholding) to the image. Defaults to False.
        blur_threshold (int, optional): The minimum acceptable variance of Laplacian for blur detection.
        Images with a variance below this threshold are considered too blurry and rejected. Defaults to 50.

    Returns:
        list: A list containing two elements:
            - The first element is a boolean indicating successful preprocessing (True) or rejection (False).
            - The second element is a string with either "ACCEPTED" or a rejection message if the image is too blurry.
    """

    # Load the image in grayscale mode for better OCR performance
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Correct skew (optional): You might need to implement the `correct_skew` function if needed
    corrected_image, skew_angle = correct_skew(img)  # Replace with your skew correction implementation

    # Apply binarization (thresholding) if desired
    if apply_binarization:
        ret, corrected_image = cv2.threshold(
            corrected_image, 127, 255, cv2.THRESH_BINARY
        )
        # Adjust the threshold value (127) and thresholding method (cv2.THRESH_BINARY) as needed

    # Apply noise reduction and contrast enhancement (optional):
    # You might want to experiment with different techniques like adaptive thresholding or histogram equalization
    corrected_image = cv2.GaussianBlur(corrected_image, (5, 5), 0)

    # Detect and reject blurry images
    var = variance_of_laplacian(corrected_image)
    if var < blur_threshold:
        return [False, "REJECTED !!! REASON : IMAGE TOO BLURRY !"]

    return [True, "ACCEPTED !!!"]
