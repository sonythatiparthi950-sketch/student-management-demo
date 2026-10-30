
class StudentManagement:
    def __init__(self):
        self.students = {}

    def add_student(self, student_id, name, age, course):
        if student_id in self.students:
            raise ValueError("Student ID already exists")

        if not name.strip():
            raise ValueError("Name cannot be empty")

        if age <= 0:
            raise ValueError("Age must be positive")

        self.students[student_id] = {
            "name": name,
            "age": age,
            "course": course
        }
        return "Student added successfully"

    def view_students(self):
        return self.students

    def search_student(self, student_id):
        return self.students.get(student_id)

    def delete_student(self, student_id):
        if student_id not in self.students:
            return False

        del self.students[student_id]
        return True


def main():
    system = StudentManagement()

    while True:
        print("\n===== Student Management System =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter your choice: ")

        try:
            if choice == "1":
                student_id = input("Student ID: ")
                name = input("Student Name: ")
                age = int(input("Student Age: "))
                course = input("Course: ")

                print(system.add_student(
                    student_id, name, age, course
                ))

            elif choice == "2":
                print(system.view_students())

            elif choice == "3":
                student_id = input("Enter Student ID: ")
                print(system.search_student(student_id))

            elif choice == "4":
                student_id = input("Enter Student ID: ")
                print("Deleted" if system.delete_student(
                    student_id
                ) else "Student not found")

            elif choice == "5":
                print("Exiting application...")
                break

            else:
                print("Invalid choice")

        except ValueError as error:
            print("Error:", error)


if __name__ == "__main__":
    main()
