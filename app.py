from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Route to handle the homepage (optional)
@app.route("/")
def index():
    return "<h1>A32i MKII Backend Running</h1><p>Ready to receive reports.</p>"

# Route to generate the report
@app.route("/generate", methods=["POST"])
def generate_report():
    data = request.get_json()
    country = data.get("country", "Unknown")

    # Placeholder content
    report_html = f"""
    <h2>A32i MKII Sustainability Report for {country}</h2>
    <p>This is a placeholder report for {country}. Replace with real data as needed.</p>
    <ul>
        <li><strong>Food Security:</strong> Example stat</li>
        <li><strong>Circular Economy:</strong> Example stat</li>
        <li><strong>Homelessness:</strong> Example stat</li>
    </ul>
    """
    return jsonify({"report": report_html})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
