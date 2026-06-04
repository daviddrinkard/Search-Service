from flask import Flask, jsonify

app = Flask(__name__)

records = [
    {"id": 1, "employee_name": "John Smith", "type": "Unauthorized Access", "severity": "High", "status": "Open"},
    {"id": 2, "employee_name": "Sarah Lee", "type": "Phishing Email", "severity": "Medium", "status": "Closed"},
    {"id": 3, "employee_name": "Bob Johnson", "type": "Policy Violation", "severity": "Low", "status": "Under Review"}
]


@app.route("/report", methods=["GET"])
def generate_report():
    report = {
        "total_records": len(records),
        "open_records": len([r for r in records if r["status"] == "Open"]),
        "closed_records": len([r for r in records if r["status"] == "Closed"]),
        "under_review_records": len([r for r in records if r["status"] == "Under Review"]),
        "high_severity_records": len([r for r in records if r["severity"] == "High"]),
        "medium_severity_records": len([r for r in records if r["severity"] == "Medium"]),
        "low_severity_records": len([r for r in records if r["severity"] == "Low"]),
        "records": records
    }

    return jsonify(report)


if __name__ == "__main__":
    app.run(port=5003)
