from flask import Flask, request, jsonify

# Create Flask App
app = Flask(__name__)

# Sample Incident Records
records = [
    {"id": 1, "type": "Unauthorized Access", "status": "Open"},
    {"id": 2, "type": "Phishing Email", "status": "Closed"},
    {"id": 3, "type": "Policy Violation", "status": "Under Review"}
]

# Search Endpoint
@app.route('/search', methods=['GET'])
def search_records():

    # Get Keyword From Request
    keyword = request.args.get('keyword')

    # Return Error If Keyword Is Missing
    if not keyword:
        return jsonify({"error": "Keyword Is Required"}), 400

    # Store Matching Results
    results = []

    # Search Through Records
    for record in records:

        # Check If Keyword Matches Record Type
        if keyword.lower() in record["type"].lower():
            results.append(record)

    # Return Matching Results
    return jsonify(results)

# Run Microservice
if __name__ == '__main__':
    app.run(port=5000)
