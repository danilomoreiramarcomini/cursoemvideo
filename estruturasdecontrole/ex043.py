weight = float(input("Type the your weight: "))
height = float(input("Type the your height: "))

bmi = weight / pow(height, 2)

if bmi < 18.5:
    print(f"\033[38mUnder weight. BMI: \033[34m{bmi:.2f}")
elif 18.5 <= bmi < 25:
    print(f"\033[38mInside the weight. BMI: \033[34m{bmi:.2f}")
elif 25 <= bmi < 30:
    print(f"\033[38mOverweight. BMI: \033[34m{bmi:.2f}")
elif 30 <= bmi < 40:
    print(f"\033[38mObese. BMI: \033[34m{bmi:.2f}")
else:
    print(f"\033[38mMorbid obese. BMI: \033[34m{bmi:.2f}")
