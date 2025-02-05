students = []

#Add Student
def add_student():
    student_id = input("Enter Student ID: ")
    name = input("Enter Student Name: ")
    age = input("Enter Student Age: ")
    course = input("Enter Student Course: ")
    
    student = {
        'ID': student_id,
        'Name': name,
        'Age': age,
        'Course': course
    }
    
    students.append(student)
    print(f"Student {name} added successfully!\n")

#Delete Student
def delete_student():
    student_id = input("Enter ID to delete::")
    for student in students:
        if student['ID']==student_id:
            students.remove(student)
            print(f"Student ID {student_id} deleted successfully!")
        else:
            print(f"Student ID {student_id} not found.")

#Update Student
def update_student():
        search = input("Enter student ID to update: ")
        for student in students:
            if student['ID']==search:
                student['ID']=input("Update the id::")
                student['Name']=input("Update the Name::")
                student['Age']=input("Update the age::")
                student['Course']=input("Update the course::")
            print(f"Student {search} updated successfully!")

#View Student
def view_student():
    student_id = input("Enter Student ID to view::")
    found = False
    for student in students:
        if student['ID'] == student_id:
            print(f"ID: {student['ID']} | Name: {student['Name']} | Age: {student['Age']} | Course: {student['Course']}")
            found = True
            break
    if not found:
        print("Student not found!\n")

#Display All Students
def display_all_students():
    if not students:
        print("No students to display!\n")
        return
    print("All Students:")
    for student in students:
        print(f"ID: {student['ID']} | Name: {student['Name']} | Age: {student['Age']} | Course: {student['Course']}")
    print()

def main():
    while True:
        print("Student Management System")
        print("1. Add Student")
        print("2. Delete Student")
        print("3. update Student")
        print("4. View Student")
        print("5. Display All Students")
        print("6. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            add_student()
        elif choice == '2':
            delete_student()
        elif choice == '3':
            update_student()
        elif choice == '4':
            view_student()
        elif choice == '5':
            display_all_students()
        elif choice == '6':
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()