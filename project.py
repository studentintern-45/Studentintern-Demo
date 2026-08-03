# ==========================================
# Employee Management System
# Developed by: Vihan Patil
# ==========================================

# List to store employee records
employees = []


# -------------------------------
# Function to Add Employee
# -------------------------------
def add_employee():
    print("\n----- Add Employee -----")

    emp_id = int(input("Enter Employee ID: "))

    # Check Duplicate ID
    for emp in employees:
        if emp["id"] == emp_id:
            print("❌ Employee ID already exists!")
            return

    name = input("Enter Name: ")
    department = input("Enter Department: ")
    age = int(input("Enter Age: "))
    salary = float(input("Enter Salary: "))

    employee = {
        "id": emp_id,
        "name": name,
        "department": department,
        "age": age,
        "salary": salary
    }

    employees.append(employee)
    print("✅ Employee Added Successfully!")


# -------------------------------
# Function to View Employees
# -------------------------------
def view_employees():

    print("\n----- Employee List -----")

    if len(employees) == 0:
        print("No employee records found.")
        return

    for emp in employees:
        print("--------------------------------")
        print(f"ID         : {emp['id']}")
        print(f"Name       : {emp['name']}")
        print(f"Department : {emp['department']}")
        print(f"Age        : {emp['age']}")
        print(f"Salary     : ₹{emp['salary']}")


# -------------------------------
# Function to Search Employee
# -------------------------------
def search_employee():

    print("\n----- Search Employee -----")

    emp_id = int(input("Enter Employee ID: "))

    for emp in employees:
        if emp["id"] == emp_id:
            print("\nEmployee Found")
            print(emp)
            return

    print("❌ Employee not found.")


# -------------------------------
# Function to Update Salary
# -------------------------------
def update_salary():

    print("\n----- Update Salary -----")

    emp_id = int(input("Enter Employee ID: "))

    for emp in employees:
        if emp["id"] == emp_id:

            print(f"Current Salary : ₹{emp['salary']}")

            new_salary = float(input("Enter New Salary: "))

            emp["salary"] = new_salary

            print("✅ Salary Updated Successfully!")
            return

    print("❌ Employee not found.")


# -------------------------------
# Function to Delete Employee
# -------------------------------
def delete_employee():

    print("\n----- Delete Employee -----")

    emp_id = int(input("Enter Employee ID: "))

    for emp in employees:
        if emp["id"] == emp_id:
            employees.remove(emp)
            print("✅ Employee Deleted Successfully!")
            return

    print("❌ Employee not found.")


# -------------------------------
# Main Menu
# -------------------------------
while True:

    print("\n===================================")
    print(" Employee Management System ")
    print("===================================")

    print("1. Add Employee")
    print("2. View All Employees")
    print("3. Search Employee by ID")
    print("4. Update Employee Salary")
    print("5. Delete Employee")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_employee()

    elif choice == "2":
        view_employees()

    elif choice == "3":
        search_employee()

    elif choice == "4":
        update_salary()

    elif choice == "5":
        delete_employee()

    elif choice == "6":
        print("\nThank you for using Employee Management System.")
        break

    else:
        print("❌ Invalid Choice! Please try again.")
