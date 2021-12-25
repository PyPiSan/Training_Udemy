'''You are going to write a program that tests the compatibility between two people.

To work out the love score between two people:

Take both people's names and check for the number of times the letters in the word TRUE occurs. 

Then check for the number of times the letters in the word LOVE occurs. 

Then combine these numbers to make a 2 digit number.

For Love Scores less than 10 or greater than 90, the message should be:'''

# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name_lower1 = name1.lower() + name2.lower()

no_of_true = (name_lower1.count("t"))+(name_lower1.count("r"))+(name_lower1.count("u"))+(name_lower1.count("e"))
no_of_love = (name_lower1.count("l"))+(name_lower1.count("o"))+(name_lower1.count("v"))+(name_lower1.count("e"))

love = int(str(no_of_true) + str(no_of_love))

if love<10 or love>90:
    print(f"Your score is {love}, you go together like coke and mentos.")
elif 50>love>40:
    print(f"Your score is {love}, you are alright together.")
else:
    print(f"Your score is {love}.")

