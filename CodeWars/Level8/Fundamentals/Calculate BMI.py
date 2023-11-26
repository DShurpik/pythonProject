def bmi(weight, height):
    bmi = weight / (height ** 2)
    result = "Underweight" if bmi <= 18.5 else "Normal" if bmi <= 25 else "Overweight" if bmi <= 30 else "Obese" if bmi > 30 else ""
    return result