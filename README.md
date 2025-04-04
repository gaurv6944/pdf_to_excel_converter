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
