Flask PDF to Excel Converter

Overview

This project is a Flask-based web application that allows users to upload a system-generated PDF file containing structured text. The app extracts table-like data from the PDF based on a key-value pattern and saves it into an Excel file for download.

Features

Upload PDF files containing structured tabular data.

Extract key-value pairs using regex pattern matching.

Save extracted data into an Excel file.

Provide a downloadable link for the processed Excel file.

Installation and Setup

Prerequisites

Ensure you have Python 3 installed on your system. Install the required dependencies using:

pip install flask pdfplumber pandas openpyxl

Running the Application

Clone or download the project.

Navigate to the project directory.

Run the following command to start the Flask application:

python app.py

Open a web browser and go to http://127.0.0.1:5001.

Code Explanation

app.py

This script initializes the Flask web application, sets up file upload directories, and handles PDF processing.

1. Import Required Libraries

import os
import re
import pdfplumber
import pandas as pd
from flask import Flask, render_template, request, send_file

os - Used for file handling (creating folders, saving files).

re - Regular expressions for pattern matching.

pdfplumber - Extracts text from PDFs.

pandas - Converts extracted data into a structured format.

flask - Provides the web application framework.

2. Setup Upload and Output Directories

UPLOAD_FOLDER = "uploads"
OUTPUT_FOLDER = "outputs"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

Creates folders to store uploaded PDFs and output Excel files if they don’t exist.

3. Function to Extract Data from PDF

def extract_table_from_pdf(pdf_path, output_excel):

Opens the PDF using pdfplumber.

Reads each page and extracts text.

Uses regular expressions to detect key: value patterns.

Converts the extracted data into a DataFrame and saves it as an Excel file.

4. Flask Routes

@app.route("/", methods=["GET", "POST"])
def index():

If a POST request is received:

It checks for the uploaded file.

Saves the file to the uploads directory.

Calls extract_table_from_pdf() to process the file.

If successful, the processed Excel file is sent back as a downloadable file.

5. Running the Flask Application

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5001))
    app.run(debug=True, port=port)

Starts the Flask application on port 5001.

Supports dynamic port assignment using environment variables.

Usage Instructions

Open the application in a web browser.

Upload a system-generated PDF containing structured text data.

Click the Transform button.

Download the generated Excel file containing extracted tables.

Limitations

Only works with text-based PDFs (not scanned images).

Requires a structured key: value format in the PDF.

May not extract complex tables accurately.

Future Enhancements

Improve table detection for irregular structures.

Support multiple table formats within a single PDF.

Enhance error handling for better user experience.

