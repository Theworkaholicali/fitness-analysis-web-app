import matplotlib.pyplot as plt
import os

def generate_charts(metrics):
    bmi = metrics["bmi"]
    score = metrics["fitness_score"]

    chart_path = "static/charts/fitness_score.png"

    plt.figure(figsize=(4,4))
    plt.bar(["Fitness Score"], [score])
    plt.ylim(0,100)
    plt.title("Overall Fitness Score")
    plt.tight_layout()
    plt.savefig(chart_path)
    plt.close()

    return {
        "fitness_score_chart": chart_path
    }
