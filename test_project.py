from project import (
    calculate_bmr,
    activity_multiplier,
    calculate_calories,
    calculate_bmi,
    interpret_bmi,
    generate_recommendation
)

# === تست تابع BMR ===
def test_calculate_bmr():
    assert calculate_bmr(25, "Male", 175, 70) == 10*70 + 6.25*175 - 5*25 + 5
    assert calculate_bmr(30, "Female", 165, 60) == 10*60 + 6.25*165 - 5*30 - 161

# === تست سطح فعالیت ===
def test_activity_multiplier():
    assert activity_multiplier("Low") == 1.2
    assert activity_multiplier("Moderate") == 1.55
    assert activity_multiplier("High") == 1.9
    assert activity_multiplier("Random") == 1.2  # تست حالت دیفالت

# === تست محاسبه کالری ===
def test_calculate_calories():
    assert calculate_calories(1500, 1.2) == round(1500 * 1.2, 2)
    assert calculate_calories(1800, 1.55) == round(1800 * 1.55, 2)

# === تست محاسبه BMI ===
def test_calculate_bmi():
    assert calculate_bmi(180, 80) == round(80 / (1.8 ** 2), 1)
    assert calculate_bmi(160, 50) == round(50 / (1.6 ** 2), 1)

# === تست تفسیر BMI ===
def test_interpret_bmi():
    assert interpret_bmi(17.5).startswith("You are underweight")
    assert interpret_bmi(22.0).startswith("Your BMI is in the normal range")
    assert interpret_bmi(27.0).startswith("You are slightly overweight")
    assert interpret_bmi(32.0).startswith("You are in the obese range")

# === تست توصیه‌ها بر اساس کالری ===
def test_generate_recommendation():
    msg = generate_recommendation(1400, "Low")
    assert "low" in msg.lower()
    assert "30 minutes" in msg

    msg = generate_recommendation(1800, "Moderate")
    assert "normal range" in msg.lower()
    assert "keep it up" in msg.lower()

    msg = generate_recommendation(2500, "High")
    assert "quite high" in msg.lower()
    assert "impressive" in msg.lower()
