weight = int(input("Enter your weight in kg: "))
height = float(input("Enter your height in m: "))

result_bmi = weight / height**2

if result_bmi < 16:
    print(f"You have underweight - {result_bmi}")
elif 16 < result_bmi < 18.5:
    print(f"You skinny person - {result_bmi}")
elif 18.5 < result_bmi < 25:
    print(f"Your bmi is normal - {result_bmi}")
elif 25 < result_bmi < 30:
    print(f"You are overweight - {result_bmi}")
elif result_bmi > 30:
    print(f"You are obese - {result_bmi}")