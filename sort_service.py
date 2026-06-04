from flask import Flask, request, jsonify

app = Flask(__name__)

records = [
    {"id": 1, "type": "Unauthorized Access", "status": "Open", "date": "2026-06-01"},
    {"id": 2, "type": "Phishing Email", "status": "Closed", "date": "2026-05-28"},
    {"id": 3, "type": "Policy Violation", "status": "Under Review", "date": "2026-06-03"},
]

@app.route("/sort", methods=["GET"])
def sort_records():
    sort_by = request.args.get("sort_by", "date")
    order = request.args.get("order", "asc")

    if sort_by not in ["id", "type", "status", "date"]:
        return jsonify({"error": "Invalid sort field"}), 400

    reverse_order = order.lower() == "desc"

    sorted_records = sorted(
        records,
        key=lambda record: record[sort_by],
        reverse=reverse_order
    )

    return jsonify(sorted_records)

if __name__ == "__main__":
    app.run(port=5002)
