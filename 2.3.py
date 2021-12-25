'''Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.

It will take your current age as the input and output a message with our time left in this format:

You have x days, y weeks, and z months left.'''

#You have x days, y weeks, and z months left.

# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
age_int = int(age)
age_in_years = 90-age_int
age_in_days= age_in_years*365
age_in_months = age_in_years*12
age_in_weeks= age_in_years*52
print(f"You have {age_in_days} days, {age_in_weeks} weeks, and {age_in_months} months left")

