import random

def get_nutrition():
    calories = random.randint(0, 201)
    fat = random.randint(0,16)
    cholesterol = random.randint(0, 41)
    sodium = random.randint(0, 701)
    carbs = random.randint(0, 50)
    protein = random.randint(0, 16)

    data = {
        "calories": calories,
        "fat": fat,
        "cholesterol": cholesterol,
        "sodium": sodium,
        "carbs": carbs,
        "protein": protein
    }

    return data
