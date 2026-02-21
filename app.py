from flask import Flask, render_template, request, jsonify
from utils.calculations import calculate_metrics
from utils.insights import generate_insights
from utils.visuals import generate_charts

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    user_data = request.json

    metrics = calculate_metrics(user_data)
    insights = generate_insights(user_data, metrics)
    charts = generate_charts(metrics)

    return jsonify({
        "metrics": metrics,
        "insights": insights,
        "charts": charts
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

