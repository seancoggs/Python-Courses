"""
Program Name: Wk5_Sean_Coggeshall.py
Student Name: Sean Coggeshall
Course: ENTD220 D002 Summer 2024
Instructor: Maxim Titley
Date: September 30, 2024
Description: This program will add exceptions into our range and calculator assignment.
Copy Wrong: This is my work

"""

import W5_Sean_Coggeshall_Mylib as sfc

# Main loop
while True:
    try:
        # Check if a range is needed
        check_range = input("Do you want to check a range for the inputs? (Y/N) ---> ").strip().upper()

        lower_range = None
        higher_range = None

        # If the user selects Y for the range
        if check_range == 'Y':
            while True:
                lower_range = float(input("Enter your Lower range ---> "))
                higher_range = float(input("Enter your Higher range ---> "))

                # Range Validation
                if lower_range > higher_range:
                    print("Error --> The lower range cannot be higher than the higher range. Please try again.")
                    continue
                break 

        while True:
            try:
                use_string_calc = input("Do you want to use string calculation? (Y/N) ---> ").strip().upper()

                if use_string_calc == 'Y':
                    calc_string = input("Enter calculation string (e.g., '20,30,*'): ")
                    result = sfc.scalc(calc_string)
                    print("Result:", result)
                    print()

                else:
                    first_number = float(input("Enter your First number ---> "))
                    second_number = float(input("Enter your Second number ---> "))

                    if check_range == 'Y':
                        if not sfc.IsInRange(lower_range, higher_range, first_number) or not sfc.IsInRange(lower_range, higher_range, second_number):
                            print("Error --> The input values are outside the allowed range.")
                            continue

                    print("The result of " + str(first_number) + " + " + str(second_number) + " = " + str(sfc.add(first_number, second_number)))
                    print("The result of " + str(first_number) + " - " + str(second_number) + " = " + str(sfc.subtract(first_number, second_number)))
                    print("The result of " + str(first_number) + " * " + str(second_number) + " = " + str(sfc.multiply(first_number, second_number)))
                    print("The result of " + str(first_number) + " / " + str(second_number) + " = " + str(sfc.divide(first_number, second_number)))
                    print()

                continue_loop = input("Do you want to perform another calculation? (Y/N) ---> ").strip().upper()
                if continue_loop != 'Y':
                    break

            except ValueError as ve:
                print(f"Error --> Invalid input: {ve}")
                continue

            except ZeroDivisionError as zde:
                print(f"Error --> {zde}")
                continue
        break

    except Exception as e:
        print(f"Error --> {e}")
        continue

print("Thanks for using our calculator!")