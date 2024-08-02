# 📄 FraudGuard: Similar Document Template Matching for Fraud Detection Using Flask

Welcome to FraudGuard, a powerful document template matching algorithm designed to automate document processing and enhance fraud detection in the healthcare domain! This project tackles the challenges faced by organizations like Bajaj Finserv Health Ltd., managing high volumes of medical invoices, prescriptions, and lab reports.

## 🚀 Project Goals

* 📝 Automate document processing tasks (text extraction, layout analysis)
* 🔍 Identify similar document templates across diverse formats
* 🕵️‍♂️ Analyze discrepancies within similar templates for potential fraud detection

## 🛠 Technical Stack

* **Front-End (Optional):**
    * 🌐 HTML, CSS, JavaScript (for user interface)
* **Back-End:**
    * 🐍 Python (core scripting language)
    * 🌶 Flask (web framework for handling requests and responses)
    * 🖼 Jinja Templating (for dynamic web pages)
* **Computer Vision Libraries:**
    * 👁 OpenCV (cv2): Image manipulation, SIFT-based template matching, layout analysis
    * 📚 EasyOCR: Optical Character Recognition (OCR) for text extraction
* **Multithreading (Optional):** Improves processing efficiency for handling multiple documents concurrently

## ⚙️ Project Functionality

1. **User Interface (Optional):** Users can upload documents and select document types (invoice, prescription, lab report).
2. **Input Validation:** The system validates the uploaded file format and size.
3. **Feature Extraction:**
    * **Text Extraction:** EasyOCR extracts text content from the uploaded document using OCR.
    * **Layout Analysis:** OpenCV (cv2) analyzes the document layout, identifying visual elements.
4. **Feature Vector Creation:** Extracted text, layout information, and visual elements are combined into a feature vector representing the document.
5. **Template Matching (SIFT):** The document's feature vector is compared against pre-defined template representations for each document type using SIFT in OpenCV. A similarity score is calculated.
6. **Match Evaluation:**
    * **High Similarity:** Documents with a high similarity score exceeding a predefined threshold proceed to fraud analysis.
    * **Low Similarity:** Documents with low similarity scores are likely not matches, and the user is notified.
7. **Fraud Analysis (High Similarity):** Critical regions specific to the document type (e.g., patient details in prescriptions) are analyzed for discrepancies.
8. **Fraud Detection:** Significant discrepancies flag the document for further manual review as potential fraud.
9. **Display Results:** The user is shown the outcome:
    * ✅ Successful match with the specific template type.
    * ❌ No match found.
    * ⚠️ Flagged for potential fraud review.

## 🌟 Benefits

* ⏳ **Reduced Manual Processing Time:** Automates document processing tasks, freeing up staff resources.
* 🎯 **Improved Accuracy:** Consistent and automated template matching reduces human error in document classification.
* 🛡 **Enhanced Fraud Detection:** Identifies potential fraudulent claims based on template discrepancies.
* 📈 **Scalability and Adaptability:** Designed for diverse document formats and can be expanded to include machine learning models for automatic classification or handling complex variations.

## 📋 Requirements

This project requires the following Python libraries:

* Flask
* Jinja2
* OpenCV-python
* easyocr

## 💻 Installation

1. Make sure you have Python 3.x installed.
2. Open a terminal or command prompt and navigate to the root directory of your project.
3. Install the required libraries using pip:

   ```bash
   pip install -r requirements.txt
   ```

## ▶️ Running the Application (Using Flask)

1. Create a file named `requirements.txt` in your project directory and add the following lines:

   ```
   Flask
   Jinja2
   OpenCV-python
   easyocr
   ```

2. Run the following command in your terminal:

   ```bash
   pip install -r requirements.txt
   ```

3. Assuming your main application script is named `flask_app.py`, run the Flask development server using:

   ```bash
   flask run
   ```

   This will start the server and make the application accessible by default at `http://127.0.0.1:5000/`.

## 📈 Further Development

* 🤖 Integrate machine learning models for automatic template classification.
* 🧩 Enhance the system's ability to learn complex variations in document formats.
* ☁️ Explore cloud deployment options for scalability.

## 🤝 Contributing

We welcome contributions to this project! Please Fork it to contribute code, report issues, and participate in the development process.

## 📜 License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).

## ⚠️ Disclaimer

This project is for educational purposes only and is not intended for production use without further testing and validation.

Enjoy exploring FraudGuard and enhancing your fraud detection capabilities! 🚀
