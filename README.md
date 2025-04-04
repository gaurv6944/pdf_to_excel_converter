 <h2>Overview</h2>
<p>This project is a Flask-based web application that allows users to upload a system-generated PDF file containing structured text. The app extracts table-like data from the PDF based on a key-value pattern and saves it into an Excel file for download.</p>

<h2>Features</h2>
<ul>
    <li>Upload PDF files containing structured tabular data.</li>
    <li>Extract key-value pairs using regex pattern matching.</li>
    <li>Save extracted data into an Excel file.</li>
    <li>Provide a downloadable link for the processed Excel file.</li>
</ul>

<h2>Installation and Setup</h2>
<h3>Prerequisites</h3>
<p>Ensure you have Python 3 installed on your system. Install the required dependencies using:</p>
<pre><code>pip install flask pdfplumber pandas openpyxl</code></pre>

<h3>Running the Application</h3>
<ol>
    <li>Clone or download the project.</li>
    <li>Navigate to the project directory.</li>
    <li>Run the following command to start the Flask application:
        <pre><code>python app.py</code></pre>
    </li>
    <li>Open a web browser and go to <code>http://127.0.0.1:5001</code>.</li>
</ol>

<h2>Code Explanation</h2>
<h3>app.py</h3>
<p>This script initializes the Flask web application, sets up file upload directories, and handles PDF processing.</p>

<h4>1. Import Required Libraries</h4>
<pre><code>import os
<h4>2. Setup Upload and Output Directories</h4>
<pre><code>UPLOAD_FOLDER = "uploads"
<h4>3. Function to Extract Data from PDF</h4>
<pre><code>def extract_table_from_pdf(pdf_path, output_excel):</code></pre>
<p>- Opens the PDF using `pdfplumber`.</p>
<p>- Reads each page and extracts text.</p>
<p>- Uses regular expressions to detect `key: value` patterns.</p>
<p>- Converts the extracted data into a DataFrame and saves it as an Excel file.</p>

<h4>4. Flask Routes</h4>
<pre><code>@app.route("/", methods=["GET", "POST"])
<h4>5. Running the Flask Application</h4>
<pre><code>if __name__ == "__main__":
port = int(os.environ.get("PORT", 5001))
app.run(debug=True, port=port)</code></pre>
<p>- Starts the Flask application on port `5001`.</p>
<p>- Supports dynamic port assignment using environment variables.</p>

<h2>Usage Instructions</h2>
<ol>
    <li>Open the application in a web browser.</li>
    <li>Upload a system-generated PDF containing structured text data.</li>
    <li>Click the <strong>Transform</strong> button.</li>
    <li>Download the generated Excel file containing extracted tables.</li>
</ol>

<h2>Limitations</h2>
<ul>
    <li>Only works with text-based PDFs (not scanned images).</li>
    <li>Requires a structured `key: value` format in the PDF.</li>
    <li>May not extract complex tables accurately.</li>
</ul>

<h2>Future Enhancements</h2>
<ul>
    <li>Improve table detection for irregular structures.</li>
    <li>Support multiple table formats within a single PDF.</li>
    <li>Enhance error handling for better user experience.</li>
</ul>
