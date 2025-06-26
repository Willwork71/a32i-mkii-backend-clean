from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/generate", methods=["POST"])
def generate_report():
    data = request.get_json()
    country = data.get("country", "Unknown")

    # Placeholder content for the report
    report_html = f"<h2>Report for {country}</h2><p>This is a dynamically generated A32i MKII sustainability report.</p>"
    return jsonify({ "report": report_html })

if __name__ == "__main__":
    app.run(debug=True)
