# AND Condition
#youth program
#allow people ages 18-25 to sign up for the program
# age = int(input("Please enter your age: "))

# if 18 <= age <= 25:
#     print("You are eligible to sign up for the youth program!")
# else:    
#     print("Sorry, you are not eligible to sign up for the youth program.")
# -------------------------------------------------------------
# OR Condition
# Regular_hours = 40
# more than 40 hours or if a holiday they get paid time and a half

totalHours = int(input("Enter total hours worked: "))
isHoliday = bool(input("Is it a holiday? (Yes/No): "))

if totalHours > 40 or isHoliday:
    print("You get paid time and a half!")
else:
    print("You get paid regular hours.")
# --------------------------------------------------------------
# NOT Condition
#voting eligibility

# age = int(input("Please enter your age: "))
# if not (age >= 18):
#     print("Sorry, you are not eligible to vote.")
# else:
#     print("You are eligible to vote!")

