from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/generate", methods=["POST"])
def generate_report():
    data = request.get_json()
    country = data.get("country", "Unknown")
    
    # Simple placeholder logic
    report_html = f"""
        <h2>A32i MKII Sustainability Report</h2>
        <p>This is a placeholder report for <strong>{country}</strong>.</p>
        <ul>
            <li><strong>Carbon Emissions:</strong> Sample Data</li>
            <li><strong>Renewable Energy %:</strong> Sample Data</li>
        </ul>
    """
    
    return jsonify({ "report": report_html })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000, debug=True)
