# BMI Calculator

def calculate_bmi(weight_kg, height_m):
    """
    Calculate Body Mass Index (BMI).
    Args:
        weight_kg (float): Weight in kilograms.
        height_m (float): Height in meters.
    Returns:
        float: Calculated BMI.
    """
    if height_m <= 0:
        raise ValueError("Height must be greater than zero.")
    return weight_kg / (height_m ** 2)


def bmi_category(bmi):
    """
    Return the BMI category for a given BMI value.
    Args:
        bmi (float): The BMI value.
    Returns:
        str: The BMI category.
    """
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"


def main():
    try:
        weight = float(input("Enter your weight in kilograms: "))
        height = float(input("Enter your height in meters: "))
        bmi = calculate_bmi(weight, height)
        category = bmi_category(bmi)
        print(f"Your BMI is: {bmi:.2f}")
        print(f"BMI Category: {category}")
    except ValueError as e:
        print(f"Invalid input: {e}")


if __name__ == "__main__":
    main()
