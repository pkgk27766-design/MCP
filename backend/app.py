from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

cloud_files = {
    "AWS S3": ["backup1.csv", "backup2.csv", "backup3.csv", "backup4.csv", "backup5.csv"],
    "Azure Blob": ["backup1.csv", "backup2.csv", "backup3.csv", "backup4.csv", "backup5.csv"],
    "GCP Bucket": ["backup1.csv", "backup2.csv", "backup3.csv", "backup4.csv"]
}

@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    question = data.get("question", "").lower()

    if "backup" in question:
        response = {
            "answer": "Backup status checked successfully.",
            "details": [
                "AWS S3 → 5 files",
                "Azure Blob → 5 files",
                "GCP Bucket → 4 files",
                "Warning: Missing file in GCP"
            ]
        }
    else:
        response = {
            "answer": "I can help with cloud backup status, file checks, and multi-cloud monitoring.",
            "details": []
        }

    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True, port=5000)