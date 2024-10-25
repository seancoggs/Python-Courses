"""
Program Name: Wk2P1_Sean_Coggeshall.py
Student Name: Sean Coggeshall
Course: ENTD220 D002 Summer 2024
Instructor: Ymmas Azaba
Date: September 9, 2024
Notes: Week 2, create a simple calculator
Copy Wrong: This is my work

"""
print('This is my first programming assignment')
first_number = input("Enter your Fist number ---> ")
second_number = input("Enter your Second number ---> ")

firstVar = float(first_number)
secondVar = float(second_number)

addition = firstVar + secondVar
subtractionn = firstVar - secondVar
multiplication = firstVar * secondVar
division = firstVar / secondVar

print("The result of " + str(first_number) + "+" + str(second_number) + "=" + str(addition))
print("The result of " + str(first_number) + "-" + str(second_number) + "=" + str(subtractionn))
print("The result of " + str(first_number) + "*" + str(second_number) + "=" + str(multiplication))
print("The result of " + str(first_number) + "/" + str(second_number) + "=" + str(division))
print()
print("Thanks for using our calculator!")