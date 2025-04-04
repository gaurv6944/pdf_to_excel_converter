<h2>Overview</h2>
<p>This Flask-based web application allows users to upload a PDF containing structured tabular data. It extracts key-value pairs and saves them in an Excel file.</p>

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
<pre><code>import os, re, pdfplumber, pandas as pd


<h4>2. Setup Directories</h4>
<pre><code>UPLOAD_FOLDER = "uploads"

<h4>5. Running the Flask App</h4>
<pre><code>if __name__ == "__main__":
app.run(debug=True, port=5001)</code></pre>

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
    <li>Requires structured `key: value` format.</li>
    <li>May not handle complex tables perfectly.</li>
</ul>

<h2>Future Enhancements</h2>
<ul>
    <li>Improve irregular table detection.</li>
    <li>Support multiple table formats.</li>
    <li>Enhance error handling.</li>
</ul>
