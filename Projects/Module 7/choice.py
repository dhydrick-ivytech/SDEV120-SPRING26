
# retry = input("Do you want to retry the quiz? (Yes/No): ")

# if retry in ["Yes", "Y", "y", "yes"]:
#     print("You have chosen to retry the quiz.")
# elif retry in ["No", "N", "n", "no"]:
#     print("You have chosen not to retry the quiz.")
# else:
#     print("Invalid input. Please enter 'Yes' or 'No'.")

import pandas as pd
empId = int(input("Enter your employee ID: "))  

if empId != -1:
    df = pd.read_csv('employee_data.csv')  
    employee_data = df[df['EmployeeID'] == empId]  
    if not employee_data.empty:
        print(employee_data)  
    else:
        print("Employee ID not found.")