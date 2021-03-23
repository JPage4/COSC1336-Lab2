#Jesse Page
#Lab 2 assignment             
#This program will take prompt the user to enter their name and birth month and year.
#The program will then output to the console a greeting with their name, what season they were born, 
# and whether or not they were born in a leap year    

# sentinel variable
control = "zzz"

# Read user's name
user_name = input("Please enter your name: ")

# input validation for user_name
while user_name != control:
    user_birth_month = int(input("Please enter your birth month: "))

    #input validation for birth month
    while user_birth_month <= 0 or user_birth_month > 12:
        print("Error, enter a valid birth month")
        user_birth_month = int(input("Please enter your birth month: "))
    
    #if-else condition to check user_birth_month and assign correct season
    if user_birth_month <= 2:
        season = "winter"
    elif user_birth_month <= 5:
        season = "spring"
    elif user_birth_month <= 8:
        season = "summer"
    elif user_birth_month <= 11:
        season = "fall"
    elif user_birth_month == 12:
        season = "winter"
    
    user_birth_year = int(input("Please enter your birth year: "))
    
    #input validation for user_birth_year
    while user_birth_year <= 0:
        print("Error, enter a valid birth year")
        user_birth_year = int(input("Please enter your birth year: "))
    
    #if-else condition to check if user_birth_year is a leap year, and the resulting print statement
    if user_birth_year % 4 == 0 and (user_birth_year % 400 == 0 or user_birth_year % 100 != 0):
        print("Hello,", user_name, end="")
        print("! You were born in the", season, end="")
        print(".",user_birth_year, "was a leap year.")
    else:
        print("Hello,", user_name, end="")
        print("! You were born in the", season, end="")
        print(".",user_birth_year, "was not a leap year.")
    user_name = control