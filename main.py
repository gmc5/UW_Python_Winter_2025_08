

# ------------------------------------------------------------------------------------------------- #
# Title: Assignment08-Starter files
# # Description: A collection of classes for managing the application
# ChangeLog: (Who, When, What)
# GMcCaslin,3.16.2025,Created Script
# ------------------------------------------------------------------------------------------------- #

import json
import processing_classes
import presentation_classes
from data_classes import Employee

# Data -------------------------------------------- #
FILE_NAME: str = 'EmployeeRatings.json'

MENU: str = '''
---- Employee Ratings ------------------------------
  Select from the following menu:
    1. Show current employee rating data.
    2. Enter new employee rating data.
    3. Save data to a file.
    4. Exit the program.
--------------------------------------------------
'''

employees: list = []  # a table of employee data
menu_choice = ''

# Beginning of the main body of this script
employees = processing_classes.FileProcessor.read_employee_data_from_file(file_name=FILE_NAME,
                                                       employee_data=employees,
                                                       employee_type=Employee)  # Note this is the class name (ignore the warning)

# Repeat the follow tasks
while True:
    presentation_classes.IO.output_menu(menu=MENU)

    menu_choice = presentation_classes.IO.input_menu_choice()

    if menu_choice == "1":  # Display current data
        try:
            presentation_classes.IO.output_employee_data(employee_data=employees)
        except Exception as e:
            presentation_classes.IO.output_error_messages(e)
        continue

    elif menu_choice == "2":  # Get new data (and display the change)
        try:
            employees = presentation_classes.IO.input_employee_data(employee_data=employees, employee_type=Employee)  # Note this is the class name (ignore the warning)
            presentation_classes.IO.output_employee_data(employee_data=employees)
        except Exception as e:
            presentation_classes.IO.output_error_messages(e)
        continue

    elif menu_choice == "3":  # Save data in a file
        try:
            processing_classes.FileProcessor.write_employee_data_to_file(file_name=FILE_NAME, employee_data=employees)
            print(f"Data was saved to the {FILE_NAME} file.")
        except Exception as e:
            presentation_classes.IO.output_error_messages(e)
        continue

    elif menu_choice == "4":  # End the program
        break  # out of the while loop
