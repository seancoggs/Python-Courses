"""
Program Name: Wk5_Sean_Coggeshall_Mylib.py
Student Name: Sean Coggeshall
Course: ENTD220 D002 Summer 2024
Instructor: Maxim Titley
Date: September 30, 2024
Description: This program will add exceptions into our range and calculator assignment.
Copy Wrong: This is my work

"""

#Range Function
def IsInRange(low_range, high_range, number):
    return low_range <= number <= high_range

#Add Function
def add(first_number, second_number):
    return first_number + second_number

#Subtraction Function
def subtract(first_number, second_number):
    return first_number - second_number

#Multiplication Function
def multiply(first_number, second_number):
    return first_number * second_number

# Division function with exception handling for division by zero
def divide(first_number, second_number):
    if second_number == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return first_number / second_number

# scalc function to parse a string input and perform the correct operation 
def scalc(p1):
    
    lstring = p1.split(",")
    num1 = float(lstring[0].strip())
    num2 = float(lstring[1].strip())
    operator = lstring[2].strip()

    if operator == "*":
        return num1 * num2
    elif operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "/":
        if num2 != 0:
            return num1 / num2
        else:
            raise ZeroDivisionError("Cannot divide by zero")
    else:
        raise ValueError("Invalid operator")
