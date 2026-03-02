import csv
import os

FILE_NAME = "students.csv"

# Create file if not exists
def initialize_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["ID", "Name", "Age", "Grade"])

# Add Student
def add_student():
    student_id = input("Enter Student ID: ")
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    grade = input("Enter Grade: ")

    with open(FILE_NAME, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([student_id, name, age, grade])

    print("✅ Student Added Successfully!")

# View All Students
def view_students():
    with open(FILE_NAME, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

# Search Student
def search_student():
    search_id = input("Enter Student ID to Search: ")
    found = False

    with open(FILE_NAME, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == search_id:
                print("Student Found:", row)
                found = True
                break

    if not found:
        print("❌ Student Not Found!")

# Delete Student
def delete_student():
    delete_id = input("Enter Student ID to Delete: ")
    rows = []
    found = False

    with open(FILE_NAME, mode='r') as file:
        reader = csv.reader(file)
        rows = list(reader)

    with open(FILE_NAME, mode='w', newline='') as file:
        writer = csv.writer(file)
        for row in rows:
            if row[0] != delete_id:
                writer.writerow(row)
            else:
                found = True

    if found:
        print("🗑 Student Deleted Successfully!")
    else:
        print("❌ Student Not Found!")

# Update Student
def update_student():
    update_id = input("Enter Student ID to Update: ")
    rows = []
    found = False

    with open(FILE_NAME, mode='r') as file:
        reader = csv.reader(file)
        rows = list(reader)

    with open(FILE_NAME, mode='w', newline='') as file:
        writer = csv.writer(file)
        for row in rows:
            if row[0] == update_id:
                print("Enter New Details:")
                name = input("Enter Name: ")
                age = input("Enter Age: ")
                grade = input("Enter Grade: ")
                writer.writerow([update_id, name, age, grade])
                found = True
            else:
                writer.writerow(row)

    if found:
        print("✏ Student Updated Successfully!")
    else:
        print("❌ Student Not Found!")

# Main Menu
def main():
    initialize_file()

    while True:
        print("\n===== Student Management System =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            search_student()
        elif choice == '4':
            update_student()
        elif choice == '5':
            delete_student()
        elif choice == '6':
            print("Exiting Program...")
            break
        else:
            print("Invalid Choice!")

if __name__ == "__main__":
    main()