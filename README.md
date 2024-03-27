# Web PDF Analyzer for Bachelor Final Projects

Web PDF Analyzer for Bachelor Final Projects is a Django-based web application designed specifically to analyze bachelor final projects in PDF format. It utilizes Tesseract OCR (Optical Character Recognition) to extract text from PDFs, enabling users to gain insights into the content of their bachelor final project documents.

## Features

- **PDF Analysis**: Upload bachelor final project PDF documents and extract keywords and summaries automatically.
- **Keyword Extraction**: Identify important keywords and phrases within bachelor final project documents.
- **Summary Generation**: Automatically generate summaries of bachelor final project documents for quick insights.
- **User Interface**: View analyzed bachelor final projects and their extracted data through a user-friendly web interface.

## Requirements

- Python 3.x
- Django
- Tesseract OCR

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your_username/web_pdf_analyzer.git
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up Tesseract OCR:
   - Follow the installation instructions for your operating system: [Tesseract OCR Installation Guide](https://github.com/tesseract-ocr/tesseract)

4. Apply migrations:
   ```bash
   python manage.py migrate
   ```

5. Run the development server:
   ```bash
   python manage.py runserver
   ```

6. Access the application at `http://localhost:8000` in your web browser.

## Usage

1. Navigate to the web interface.
2. Upload a bachelor final project PDF document using the provided form.
3. Wait for the analysis to complete.
4. View the extracted keywords and summary for the uploaded bachelor final project.
5. Repeat the process for additional bachelor final project PDF documents as needed.
