class Person:
    def __init__(self, name="", age=0):
        self.name = name
        self.age = age

    def display(self):
        print("\nPerson Details:")
        print("Name -_- ", self.name)
        print("Age -_- ", self.age)


class Employee(Person):
    def __init__(self, name="", age=0, emp_id="", salary=0):
        super().__init__(name, age)
        self.emp_id = emp_id       # removed __ (private)
        self.salary = salary

    def display(self):
        print("\nEmployee Details -_- ")
        print("Name -_- ", self.name)
        print("Age -_- ", self.age)
        print("Employee ID -_- ", self.emp_id)
        print("Salary -_- $", self.salary)


class Manager(Employee):
    def __init__(self, name="", age=0, emp_id="", salary=0, department=""):
        super().__init__(name, age, emp_id, salary)
        self.department = department

    def display(self):
        super().display()
        print("Department -_- ", self.department)


class Developer(Employee):
    def __init__(self, name="", age=0, emp_id="", salary=0, language=""):
        super().__init__(name, age, emp_id, salary)
        self.language = language

    def display(self):
        super().display()
        print("Programming Language -_- ", self.language)


def main():
    person = None
    employee = None
    manager = None

    while True:
        print("\n--- Python OOP Project: Employee Management System ---")
        print("1. Create a Person")
        print("2. Create an Employee")
        print("3. Create a Manager")
        print("4. Show Details")
        print("5. Exit")

        choice = input("Enter your choice -_- ")

        if choice == "1":
            name = input("Enter Name -_- ")
            age = int(input("Enter Age -_- "))
            person = Person(name, age)
            print("\nPerson created successfully!")

        elif choice == "2":
            name = input("Enter Name -_- ")
            age = int(input("Enter Age -_- "))
            emp_id = input("Enter Employee ID -_- ")
            salary = float(input("Enter Salary -_- "))
            employee = Employee(name, age, emp_id, salary)
            print("\nEmployee created successfully!")

        elif choice == "3":
            name = input("Enter Name -_- ")
            age = int(input("Enter Age -_- "))
            emp_id = input("Enter Employee ID -_- ")
            salary = float(input("Enter Salary -_- "))
            dept = input("Enter Department -_- ")
            manager = Manager(name, age, emp_id, salary, dept)
            print("\nManager created successfully!")

        elif choice == "4":
            print("\n1. Person\n2. Employee\n3. Manager")
            sub = input("Choose details to show -_- ")

            if sub == "1" and person:
                person.display()
            elif sub == "2" and employee:
                employee.display()
            elif sub == "3" and manager:
                manager.display()
            else:
                print("No data found!")

        elif choice == "5":
            print("\nExiting the system. Goodbye!")
            break

        else:
            print("Invalid choice! Try again.")


# Run Program
main()
