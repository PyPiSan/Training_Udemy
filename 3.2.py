'''Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.

It should tell them the interpretation of their BMI based on the BMI value.

Under 18.5 they are underweight
Over 18.5 but below 25 they have a normal weight
Over 25 but below 30 they are slightly overweight
Over 30 but below 35 they are obese
Above 35 they are clinically obese.'''

height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

#The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):

bmi = round(weight/(height**2))
if bmi<18.5:
    print("Your BMI is {}, you are underweight.".format(bmi))
elif 25>bmi>=18.5:
    print("Your BMI is {}, you have a normal weight.".format(bmi))
elif 30>bmi>=25:
    print("Your BMI is {}, you are slightly overweight.".format(bmi))
elif 35>bmi>=30:
    print("Your BMI is {}, you are obese.".format(bmi))
else:
    print("Your BMI is {}, you are clinically obese.".format(bmi))

