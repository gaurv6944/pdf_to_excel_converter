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
