import os
import re
import pdfplumber
import pandas as pd
from flask import Flask, render_template, request, send_file

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
OUTPUT_FOLDER = "outputs"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

def extract_table_from_pdf(pdf_path, output_excel):
    extracted_data = []
    
    try:
        with pdfplumber.open(pdf_path) as pdf:
            for i, page in enumerate(pdf.pages):
                text = page.extract_text()
                if not text:
                    continue  # Skip empty pages
                
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
        return False

@app.route("/", methods=["GET", "POST"])
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

    return render_template("index.html")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5001))  # Run on dynamic port
    app.run(debug=True, port=port)

