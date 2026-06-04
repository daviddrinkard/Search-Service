from flask import Flask, jsonify

app = Flask(__name__)

records = [
    {"id": 1, "type": "Unauthorized Access", "status": "Open", "date": "2026-06-01"},
    {"id": 2, "type": "Phishing Email", "status": "Closed", "date": "2026-05-28"},
    {"id": 3, "type": "Policy Violation", "status": "Under Review", "date": "2026-06-03"},
]

@app.route("/report", methods=["GET"])
def generate_report():
    report = {
        "total_records": len(records),
        "open_records": len([r for r in records if r["status"] == "Open"]),
        "closed_records": len([r for r in records if r["status"] == "Closed"]),
        "under_review_records": len([r for r in records if r["status"] == "Under Review"]),
        "records": records
    }

    return jsonify(report)

if __name__ == "__main__":
    app.run(port=5003)
