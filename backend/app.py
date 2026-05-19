from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

cloud_files = {
    "AWS S3": ["backup1.csv", "backup2.csv", "backup3.csv", "backup4.csv", "backup5.csv"],
    "Azure Blob": ["backup1.csv", "backup2.csv", "backup3.csv", "backup4.csv", "backup5.csv"],
    "GCP Bucket": ["backup1.csv", "backup2.csv", "backup3.csv", "backup4.csv"]
}

@app.route("/", methods=["GET"])
def home():
    return "Backend is running successfully"

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

    elif "deployment" in question:
        response = {
            "answer": "Deployment analysis completed.",
            "details": [
                "Frontend container is running",
                "Backend API is running",
                "Docker deployment is successful",
                "Recommendation: Deploy next to AWS ECS Fargate"
            ]
        }

    elif "alert" in question:
        response = {
            "answer": "Alert analysis completed.",
            "details": [
                "Azure VM shows high CPU usage",
                "Database has connection delay",
                "AWS ECS and GCP Storage are healthy",
                "Recommendation: create CloudWatch alarm and SNS email alert"
            ]
        }

    elif "log" in question:
        response = {
            "answer": "Log summary generated.",
            "details": [
                "Frontend Nginx started successfully",
                "Backend Flask API is responding",
                "No critical container errors found",
                "Recommendation: enable centralized logging"
            ]
        }

    elif "incident" in question:
        response = {
            "answer": "Incident detection completed.",
            "details": [
                "Possible issue detected in Azure VM CPU usage",
                "Database delay may affect application response time",
                "Priority: Medium",
                "Suggested action: monitor CPU and database latency"
            ]
        }

    elif "optimization" in question:
        response = {
            "answer": "Optimization advice generated.",
            "details": [
                "Use auto-scaling for production workloads",
                "Enable container health checks",
                "Optimize backend API response time",
                "Use CloudWatch metrics for performance tuning"
            ]
        }

    elif "cost" in question:
        response = {
            "answer": "Cost analysis completed.",
            "details": [
                "Avoid NAT Gateway for test environment",
                "Stop unused containers and cloud resources",
                "Use Fargate only when required",
                "Set billing alerts to control AWS cost"
            ]
        }

    elif "troubleshooting" in question:
        response = {
            "answer": "Troubleshooting completed.",
            "details": [
                "Check frontend container status",
                "Check backend API on port 5000",
                "Verify fetch URL in dashboard.html",
                "Rebuild Docker containers after code changes"
            ]
        }

    else:
        response = {
            "answer": "I can help with cloud backup status, alerts, deployment, logs, cost, optimization, and troubleshooting.",
            "details": []
        }

    return jsonify(response)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5000)