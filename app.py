from flask import Flask, request, render_template, send_file
import os
from data_cleaner import clean_data  # Ensure you have the data_cleaner module that contains the clean_data function

app = Flask(__name__)
UPLOAD_FOLDER = "static/cleaned_files/"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        file = request.files["file"]
        if file:
            file_path = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(file_path)

            # Clean the file
            cleaned_df = clean_data(file_path)

            # Save the cleaned file
            cleaned_file_path = os.path.join(UPLOAD_FOLDER, f"cleaned_{file.filename}")
            if file.filename.endswith(".csv"):
                cleaned_df.to_csv(cleaned_file_path, index=False)
            else:
                cleaned_df.to_excel(cleaned_file_path, index=False)

            # Send the cleaned file as a download
            return send_file(cleaned_file_path, as_attachment=True)

    return render_template("upload.html")

if __name__ == "__main__":
    app.run(debug=True)
