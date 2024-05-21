import cv2
import os
from concurrent.futures import ThreadPoolExecutor
from PIL import Image


def delete_icc_profile(image_path):
    """
    Removes the ICC profile from a PNG image using Pillow.

    Args:
        image_path (str): Path to the image file.
    """

    # Open the image using Pillow
    img = Image.open(image_path)

    # Access the image metadata dictionary
    info = img.info

    # Check if the 'icc_profile' key exists in the metadata
    if "icc_profile" in info:
        # If it exists, remove the ICC profile data using pop
        info.pop("icc_profile", None)

    # Save the image back to the same path without the ICC profile
    img.save(image_path)


def preprocess_image(image_path):
    """
    Preprocesses an image for template matching, removing the ICC profile first.

    Args:
        image_path (str): Path to the image file.

    Returns:
        np.ndarray: Grayscale and resized image for template matching.
    """

    # Remove the ICC profile before further processing
    delete_icc_profile(image_path)

    # Read the image in BGR color space using OpenCV (without ICC profile)
    image = cv2.imread(image_path)

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Resize the image to the desired dimensions
    # Modify resize dimensions as needed
    resized = cv2.resize(gray, (256, 256))

    # Now return resized image
    return resized


def detect_and_match_features(image, template):
    """
    Detects features and performs matching between an image and a template.

    Args:
        image (np.ndarray): The preprocessed image as a NumPy array.
        template (np.ndarray): The preprocessed template image as a NumPy array.

    Returns:
        int: The number of good matches between the image and the template.
    """

    # Choose a feature detector (uncomment your preferred choice)
    detector = cv2.SIFT_create()  # type: ignore # SIFT (slower, more accurate)
    # detector = cv2.ORB_create()  # ORB (faster, often recommended)

    # Detect keypoints and compute descriptors
    kp1, des1 = detector.detectAndCompute(image, None)
    kp2, des2 = detector.detectAndCompute(template, None)

    # Match descriptors using FLANN matcher
    matcher = cv2.FlannBasedMatcher(dict(algorithm=1, trees=5), dict(checks=50))
    matches = matcher.knnMatch(des1, des2, k=2)

    # Filter good matches based on Lowe's ratio test
    good_matches = [m for m, n in matches if m.distance < 0.7 * n.distance]

    # Return the number of good matches
    return len(good_matches)


def compare_with_template(image, template_path, threshold=15):
    """
    Compares a preprocessed image with a single template image and returns True if the
    number of good matches between them exceeds a specified threshold.

    Args:
        image (np.ndarray): The preprocessed image as a NumPy array. It's assumed
                           that the image has already been processed using a function
                           like `preprocess_image` (not shown here) to improve feature
                           extraction and matching performance.
        template_path (str): The path to the template image file.
        threshold (int, optional): The minimum number of good matches required for
                                   the image to be considered a match to the template.
                                   Defaults to 15.

    Returns:
        bool: True if the number of good matches is greater than or equal to the
              threshold, False otherwise.
    """

    # Preprocess the template image (if necessary)
    template = preprocess_image(template_path)

    # Detect features and perform matching between image and template
    num_matches = detect_and_match_features(image, template)

    # Compare the number of good matches with the threshold
    return num_matches >= threshold


def compare_image_with_templates(
    image_path, template_folder, threshold=15, num_threads=4
):
    """
    Compares an image with templates in a folder using multithreading and early stopping.

    Args:
        image_path (str): Path to the image.
        template_folder (str): Path to the template folder containing template image files.
        threshold (int, optional): Minimum number of good matches for a passing result (default: 15).
        num_threads (int, optional): Number of threads to use for parallel template matching (default: 4).

    Returns:
        list: A list containing two elements:
            - The first element is a boolean indicating successful matching (True) or rejection (False).
            - The second element is a string with either "ACCEPTED !" or a rejection message if no templates matched.
    """

    # Preprocess the image before template matching
    image = preprocess_image(image_path)  # Assumes preprocess_image function exists

    # Use ThreadPoolExecutor for multithreaded template matching
    with ThreadPoolExecutor(max_workers=num_threads) as executor:

        # Iterate through template files in the folder
        for filename in os.listdir(template_folder):
            if filename.endswith(".png"):
                template_path = os.path.join(template_folder, filename)
                # Submit a task (future) to compare the image with the current template
                future = executor.submit(
                    compare_with_template, image, template_path, threshold
                )

                # stopping: If a match is found, return "passed" immediately
                if future.result():
                    return [True, "ACCEPTED !!! "]

        # No match found in all templates
        return [False, "REJECTED !!! REASON : IMAGE NOT MATCHED DURING TEMPLATE MATCHING PROCESS ! "]
