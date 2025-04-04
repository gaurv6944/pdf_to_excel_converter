 <h2>1. Install Required Dependencies</h2>
Ensure you have Python 3 installed on your system. Install the required dependencies using the following command:

sh
Copy
Edit
pip install flask pdfplumber pandas openpyxl
<h2>2. Set Up the Project Structure</h2>
Create a folder for your project and inside it, ensure you have:

app.py (Main Flask application)

templates/index.html (HTML template for the UI)

uploads/ (Directory to store uploaded PDFs)

outputs/ (Directory to store extracted Excel files)

<h2>3. Run the Flask Application</h2>
Navigate to the project directory in your terminal or command prompt and run:

sh
Copy
Edit
python app.py
This starts the Flask web server on http://127.0.0.1:5001.

<h2>4. Access the Web Application</h2>
Open a web browser and go to:

cpp
Copy
Edit
http://127.0.0.1:5001
<h2>5. Upload a PDF File</h2>
Click on the "Choose File" button.

Select a structured PDF file (must contain key: value format data).

Click "Transform" to process the file.

<h2>6. Extract and Download Data</h2>
The application will extract the structured data from the PDF.

If successful, it will provide a download link for the Excel file.

Click on the download link to save the Excel file to your computer.

<h2>7. Check the Output</h2>
The extracted data is saved as an Excel file (extracted_data.xlsx) inside the outputs/ directory.

Open the file using Microsoft Excel or Google Sheets.

<h2>8. Stop the Flask Server</h2>
To stop the running server, go back to the terminal where Flask is running and press:

objectivec
Copy
Edit
CTRL + C
<h2>Understanding the Code Execution Flow</h2>
Flask initializes the app and sets up the necessary directories (uploads/ and outputs/).

The user uploads a PDF file through the web interface.

The file is saved in the uploads/ directory.

extract_table_from_pdf() function processes the file:

Reads the PDF text using pdfplumber.

Uses regex matching to extract key: value pairs.

Converts the extracted data into an Excel file.

If the extraction is successful, the Excel file is made available for download.

If no structured data is found, an error message is displayed.

<h2>Limitations</h2>
This application only works with text-based PDFs (not scanned images).

The data format in the PDF must follow key: value pairs for accurate extraction.

May struggle with complex tables that do not have a structured format.

<h2>Future Enhancements</h2>
Improve table detection for PDFs with irregular structures.

Support multiple table formats (e.g., column-based tables).

Better error handling to avoid failures in certain PDF formats.
