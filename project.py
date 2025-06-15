from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/result', methods=['POST'])
def result():
    age = int(request.form['age'])
    gender = request.form['gender']
    
    height = float(request.form['height'])
    height_unit = request.form['height_unit']
    if height_unit == 'inch':
        height *= 2.54  # تبدیل اینچ به سانتی‌متر

    weight = float(request.form['weight'])
    weight_unit = request.form['weight_unit']
    if weight_unit == 'lbs':
        weight *= 0.453592  # تبدیل پوند به کیلوگرم

    activity_level = request.form['activity_level']

    # محاسبه کالری
    bmr = calculate_bmr(age, gender, height, weight)
    multiplier = activity_multiplier(activity_level)
    calories = calculate_calories(bmr, multiplier)

    recommendation = generate_recommendation(calories, activity_level)

    # محاسبه BMI
    bmi = calculate_bmi(height, weight)
    bmi_message = interpret_bmi(bmi)

    return render_template("result.html", calories=calories, recommendation=recommendation, bmi=bmi, bmi_message=bmi_message)

def calculate_bmr(age, gender, height, weight):
    if gender == "Male":
        return 10 * weight + 6.25 * height - 5 * age + 5
    else:
        return 10 * weight + 6.25 * height - 5 * age - 161

def activity_multiplier(level):
    levels = {
        "Low": 1.2,
        "Moderate": 1.55,
        "High": 1.9
    }
    return levels.get(level, 1.2)

def calculate_calories(bmr, multiplier):
    return round(bmr * multiplier, 2)

def calculate_bmi(height_cm, weight_kg):
    height_m = height_cm / 100
    bmi = weight_kg / (height_m ** 2)
    return round(bmi, 1)

def interpret_bmi(bmi):
    if bmi < 18.5:
        return "You are underweight. A balanced diet may help you reach a healthier weight."
    elif 18.5 <= bmi < 25:
        return "Your BMI is in the normal range. Keep up the good work!"
    elif 25 <= bmi < 30:
        return "You are slightly overweight. Consider regular physical activity and a balanced diet."
    else:
        return "You are in the obese range. It's important to consult a healthcare provider for guidance."

def generate_recommendation(calories, activity_level):
    message = ""

    if calories < 1500:
        message += "Your daily calorie intake seems low. Make sure you're getting enough nutrients."
    elif calories <= 2000:
        message += "Your calorie level is within a normal range. Keep maintaining a balanced diet."
    else:
        message += "Your daily calorie intake is quite high. Consider adjusting your diet or increasing physical activity."

    if "Low" in activity_level:
        message += " Try to include at least 30 minutes of light physical activity per day."
    elif "Moderate" in activity_level:
        message += " Great! Your activity level is moderate. Keep it up!"
    elif "High" in activity_level:
        message += " Impressive! Make sure you're getting enough calories to match your activity level."

    return message


if __name__ == "__main__":
    app.run(debug=True)
