import numpy as np

def calculate_metrics(data):
    weight = float(data["weight"])
    height_m = float(data["height"]) / 100
    age = int(data["age"])
    gender = data["gender"]
    activity = data["activity"]
    goal = data["goal"]

    bmi = round(weight / (height_m ** 2), 1)

    if gender == "male":
        bmr = 10 * weight + 6.25 * (height_m * 100) - 5 * age + 5
    else:
        bmr = 10 * weight + 6.25 * (height_m * 100) - 5 * age - 161

    activity_factor = {
        "sedentary": 1.2,
        "moderate": 1.55,
        "active": 1.75
    }[activity]

    calories = int(bmr * activity_factor)

    if goal == "fat_loss":
        calories -= 400
    elif goal == "muscle_gain":
        calories += 300

    fitness_score = int(
        np.clip(
            100 - abs(22 - bmi) * 2 - (30 - age) * 0.3,
            40,
            95
        )
    )

    return {
        "bmi": bmi,
        "bmr": int(bmr),
        "daily_calories": calories,
        "fitness_score": fitness_score
    }
