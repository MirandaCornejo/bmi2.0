height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

bmi= weight/height**2
a=(round(bmi))

if bmi <= 18.5:
    print(f"Your \033 BMI \033 is {a} , you are underweight")
elif bmi >18.5 and bmi<25:
    print(f"Your \033 BMI \033 is {a} , you have a normal weight")
elif bmi>25 and bmi<30:
    print(f"Your \033 BMI \033 is {a} , you are slightly overweight")
elif bmi>30 and bmi<35:
    print(f"Your \033 BMI \033 is {a} , you are obese")
else:
    print(f"Your \033 BMI \033 is {a} , you are clinically obese") 