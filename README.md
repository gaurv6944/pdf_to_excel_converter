
<h2>Features</h2>
<ul>
    <li>Upload PDF files with structured tables.</li>
    <li>Extract key-value pairs using regex.</li>
    <li>Convert extracted data into Excel format.</li>
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
<h3>app.py</h3>
<h4>1. Import Libraries</h4>
<pre><code>import os


import re import pdfplumber import pandas as pd from flask import Flask, render\_template, request, send\_file


<h4>2. Setup Directories</h4>
<pre><code>UPLOAD_FOLDER = "uploads"


OUTPUT\_FOLDER = "outputs" os.makedirs(UPLOAD\_FOLDER, exist\_ok=True) os.makedirs(OUTPUT\_FOLDER, exist\_ok=True)


<h4>3. Define Extraction Function</h4>
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

<h4>4. Define Flask Routes</h4>
<pre><code>@app.route("/", methods=["GET", "POST"])


def index(): if request.method == "POST": if "file" not in request.files: return "No file uploaded", 400 file = request.files["file"] if file.filename == "": return "No selected file", 400 file\_path = os.path.join(UPLOAD\_FOLDER, file.filename) file.save(file\_path) output\_excel = os.path.join(OUTPUT\_FOLDER, "extracted\_data.xlsx") success = extract\_table\_from\_pdf(file\_path, output\_excel) if success: return send\_file(output\_excel, as\_attachment=True) else: return "No structured data found in the PDF", 400 return render\_template("index.html")

<h4>5. Running the Flask App</h4>
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


