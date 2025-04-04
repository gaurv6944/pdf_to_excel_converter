 <!DOCTYPE html>
<html>
<head>
    <title>Flask PDF to Excel Converter - README</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; padding: 20px; }
        h2, h3, h4 { color: #333; }
        pre { background: #f4f4f4; padding: 10px; border-radius: 5px; overflow-x: auto; }
        code { font-family: Consolas, monospace; color: #d63384; }
    </style>
</head>
<body>

    <h2>Flask PDF to Excel Converter</h2>

    <h2>Overview</h2>
    <p>This Flask-based web application allows users to upload a PDF containing structured tabular data. It extracts key-value pairs and saves them in an Excel file.</p>

    <h2>Features</h2>
    <ul>
        <li>Upload PDF files containing structured tables.</li>
        <li>Extract key-value pairs using regex.</li>
        <li>Convert extracted data into an Excel file.</li>
        <li>Download the generated Excel file.</li>
    </ul>

    <h2>Installation & Setup</h2>
    <h3>Prerequisites</h3>
    <p>Ensure Python 3 is installed. Install dependencies:</p>
    <pre><code>pip install flask pdfplumber pandas openpyxl</code></pre>

    <h3>Running the Application</h3>
    <ol>
        <li>Clone or download the project.</li>
        <li>Navigate to the directory and run:
            <pre><code>python app.py</code></pre>
        </li>
        <li>Open <code>http://127.0.0.1:5001</code> in a browser.</li>
    </ol>

    <h2>Code Explanation</h2>

    <h3>1. Import Required Libraries</h3>
    <pre><code>import os
import re
import pdfplumber
import pandas as pd
from flask import Flask, render_template, request, send_file</code></pre>

    <h3>2. Setup Flask App and Directories</h3>
    <pre><code>app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
OUTPUT_FOLDER = "outputs"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)</code></pre>

    <h3>3. Function to Extract Tables from PDF</h3>
    <pre><code>def extract_table_from_pdf(pdf_path, output_excel):
    extracted_data = []
    try:
        with pdfplumber.open(pdf_path) as pdf:
            for i, page in enumerate(pdf.pages):
                text = page.extract_text()
                if not text:
                    continue
                lines = text.split("\n")
                table_data = {}
                for line in lines:
                    match = re.match(r"([\w\s]+)\s+:\s+(.+)", line)
                    if match:
                        key, value = match.groups()
                        table_data[key.strip()] = value.strip()
                if table_data:
                    extracted_data.append(table_data)
        if extracted_data:
            df = pd.DataFrame(extracted_data)
            df.to_excel(output_excel, index=False)
            return True
        return False
    except Exception as e:
        print(f"Error extracting table: {e}")
        return False</code></pre>

    <h3>4. Flask Route to Handle File Uploads</h3>
    <pre><code>@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if "file" not in request.files:
            return "No file uploaded", 400
        file = request.files["file"]
        if file.filename == "":
            return "No selected file", 400
        file_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(file_path)
        output_excel = os.path.join(OUTPUT_FOLDER, "extracted_data.xlsx")
        success = extract_table_from_pdf(file_path, output_excel)
        if success:
            return send_file(output_excel, as_attachment=True)
        else:
            return "No structured data found in the PDF", 400
    return render_template("index.html")</code></pre>

    <h3>5. Running the Flask App</h3>
    <pre><code>if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5001))
    app.run(debug=True, port=port)</code></pre>

    <h2>Usage</h2>
    <ol>
        <li>Open the web app.</li>
        <li>Upload a structured PDF file.</li>
        <li>Click <strong>Transform</strong> to extract tables.</li>
        <li>Download the generated Excel file.</li>
    </ol>

    <h2>Limitations</h2>
    <ul>
        <li>Only works with text-based PDFs.</li>
        <li>Requires structured <code>key: value</code> format.</li>
        <li>May not handle complex tables perfectly.</li>
    </ul>

    <h2>Future Enhancements</h2>
    <ul>
        <li>Improve irregular table detection.</li>
        <li>Support multiple table formats.</li>
        <li>Enhance error handling.</li>
    </ul>

</body>
</html>
