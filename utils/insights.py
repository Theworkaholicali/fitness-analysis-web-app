def generate_insights(user, metrics):
    tips = []

    bmi = metrics["bmi"]
    score = metrics["fitness_score"]
    workouts = int(user["workouts"])

    if bmi > 25:
        tips.append("Focus on calorie control and daily movement. Fat loss should be your priority.")
    elif bmi < 18.5:
        tips.append("You need to increase calorie intake and strength training.")

    if workouts < 3:
        tips.append("Increase workout frequency to at least 3 days per week.")
    else:
        tips.append("Your workout consistency is solid. Progressively overload.")

    if score < 60:
        tips.append("Sleep, hydration, and consistency will improve your overall fitness score.")
    else:
        tips.append("You are on the right track. Maintain discipline and recovery.")

    return tips
