import re
import easyocr
from Keywords import (
    invoice_keywords,
    prescription_keywords,
    lab_report_keywords,
    general_keywords,
)
def process_ocr(image_path):
    """
    Processes a single image using Optical Character Recognition (OCR).

    Args:
        image_path: Path to the image file.

    Returns:
        str: Extracted text from the image.
    """

    # Initialize EasyOCR reader
    reader = easyocr.Reader(['en'])

    try:
        # Perform OCR
        result = reader.readtext(image_path)

        # Extract text from the result
        extracted_text = ' '.join([text[1] for text in result])

        return extracted_text

    # Handle errors during OCR processing
    except Exception as e:
        return f"Error: {e}"
    
def preprocess_text(text):
    """
    Preprocesses text by converting to lowercase, removing punctuation, and fixing typos (optional).

    Args:
        text: The text to be preprocessed.

    Returns:
        list: A list of words representing the preprocessed text.
    """

    text = text.lower()
    text = text.split()  # Split text into a list of words
    text = list(filter(lambda item: (item.isalpha() and len(item)>1), text))
    return text

def check_keywords(text, keywords, threshold=0.05):
    """
    Checks for keyword matches in preprocessed text and compares against a threshold.

    Args:
        text: The preprocessed text as a list of words.
        keywords: A list of keywords to match against.
        threshold (optional): The minimum percentage of keywords that must be matched for successful classification (default: 0.05).

    Returns:
        bool: True if the percentage of matched keywords is greater than or equal to the threshold, False otherwise.
    """
    matches = 0
    for keyword in keywords:
        if keyword in text:
            matches += 1
    return matches / len(keywords) >= threshold

def classify_document(text,keywords_list,threshold=0.05):
    """
    Classifies a document based on document type, keyword list, and threshold.

    Args:
        text: The preprocessed text as a list of words.
        document_type: The expected document type (e.g., "invoice", "prescription", "lab_report").
        keywords_dict: A dictionary mapping document types to their keyword lists.
        threshold (optional): The minimum percentage of keywords that must be matched for successful classification (default: 0.05).

    Returns:
        bool: True if the document classification is successful based on keyword matching, False otherwise.
    """
    preprocessed_text = preprocess_text(text)
    
    if keywords_list:
        return check_keywords(preprocessed_text, keywords_list, threshold)  # Check for matches
    else:
        return False  # Document type not found or no keywords defined

def OCR_MATCHING(document_type, image_path):
    """
    This function performs document classification using Optical Character Recognition (OCR).

    Args:
        document_type (str): The type of document to be classified (e.g., "invoice", "prescription", "lab_report").
        image_path (str): The path to the image file containing the document text.

    Returns:
        list: A list containing two elements:
            - The first element is a boolean indicating classification success (True) or failure (False).
            - The second element is a string with the classification result or a rejection message.
    """

    # Define a dictionary mapping document types to their keywords
    keywords_dict = {
        "invoice": invoice_keywords + general_keywords,
        "prescription": prescription_keywords + general_keywords,
        "lab_report": lab_report_keywords + general_keywords
        # Add other document types with their keyword lists here
    }
    # Set a threshold for keyword matching accuracy (e.g., 0.05 for 5%)
    threshold = 0.05  # Adjust this value as needed
    
    # Extract text from the image using an external OCR process (not shown)
    extracted_text = process_ocr(image_path)

    # Check if extracted text is empty (no characters)
    if not re.search(r'\w', extracted_text):
        return [False, "REJECTED !!! REASON : IMAGE NOT READABLE ! "]  # Indicate rejection

    # Check if extracted text is a string (not an error message)
    if isinstance(extracted_text, str):
        classified = classify_document(extracted_text, keywords_dict[document_type], threshold)

        return [True, "ACCEPTED !!!"] if classified else [False, "REJECTED !!! REASON : IMAGE NOT MATCHED DURING OCR MATCHING ! "]
    else:
        return [False, extracted_text]
