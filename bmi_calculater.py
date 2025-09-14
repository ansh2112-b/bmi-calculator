def calculate_bmi(weight, height):
    """Function to calculate BMI"""
    bmi = weight / (height ** 2)
    return bmi


def classify_bmi(bmi):
    """Function to classify BMI into categories"""
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"


def main():
    print("=== BMI Calculator ===")

    # User input validation for weight
    while True:
        weight_input = input("Enter your weight in kilograms: ")
        try:
            weight = float(weight_input)
            if weight > 0:
                break
            else:
                print("❌ Weight must be greater than 0.\n")
        except ValueError:
            print("❌ Invalid input! Please enter a number.\n")

    # User input validation for height
    while True:
        height_input = input("Enter your height in meters: ")
        try:
            height = float(height_input)
            if height > 0:
                break
            else:
                print("❌ Height must be greater than 0.\n")
        except ValueError:
            print("❌ Invalid input! Please enter a number.\n")

    # BMI calculation
    bmi = calculate_bmi(weight, height)

    # Categorization
    category = classify_bmi(bmi)

    # Output
    print(f"\nYour BMI is: {bmi:.2f}")
    print(f"Category: {category}")


if __name__=="__main__":
    main()
