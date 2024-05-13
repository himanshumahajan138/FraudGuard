# Import necessary functions from other files
import os
from Convert_To_Png import convert_to_png
from Pre_Processing import preprocess_image
from OCR_Matching import OCR_MATCHING
from Template_Matching import compare_image_with_templates



def CHECK(document_type, image_path):
    """
    This function performs document type checking and processing.

    Args:
        document_type (str): The type of document to be processed (e.g., "invoice", "prescription", "labreport").
        image_path (str): The path to the image file.

    Returns:
        str: A message indicating the result of processing, including success or error messages.
    """

    template_folders = {
            "invoice": r"INVOICES",
            "prescription": r"PRESCRIPTIONS",
            "labreport": r"LABREPORTS"
        }
    
    
    # Check if the image path exists and is a file
    if not os.path.exists(image_path) or not os.path.isfile(image_path):
        return "REJECTED !!! REASON : IMAGE DON'T EXIST !"
        # return render_template('result.html', result=result)
    
    # Set threshold value based on document type
    thresholds = {
        "invoice": 15,
        "prescription": 20,
        "labreport": 25,
    }

    document_type=document_type.lower()
    
    threshold = thresholds.get(document_type, 15)  # Use default if type not in thresholds
    
    # Convert the image to PNG format if necessary
    if not image_path.endswith(".png"):
        image_path = convert_to_png(image_path)
        if (image_path == False):
            return "REJECTED !!! REASON : INVALID IMAGE FORMAT !"

    # Steps of processing image and extraction
    preprocessed_img = preprocess_image(image_path)
    
    if not preprocessed_img[0]:  # Check if preprocessing was successful
        return preprocessed_img[1]  # Print preprocessing error message

    OCR_RESULT = OCR_MATCHING(document_type, image_path)

    if not OCR_RESULT[0]:  # Check if OCR was successful
        return OCR_RESULT[1]  # Print OCR error message

    template_folder = template_folders[document_type]
    # Template matching (after successful OCR)
    matched = compare_image_with_templates(image_path, template_folder, threshold, num_threads=4)
    
    return matched[1]  # Return template matching message or other result
