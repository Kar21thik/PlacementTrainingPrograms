class Student:
    idGenerator = 101  # Static variable

    def __init__(self, name='', marks=0):
        self.id = Student.idGenerator
        self.name = name
        self.marks = marks
        Student.idGenerator += 1

    def __str__(self):
        return f'ID: {self.id}, Name: {self.name}, Marks: {self.marks}'


class StudentOperations:
    def createStudent(self, students):
        name = input("Enter name of the student: ")
        marks = int(input('Enter marks of the student: '))
        students.append(Student(name, marks))

    def listStudent(self, students):
        print('%-5s %-15s %-3s' % ('ID', 'Name', 'Marks'))
        print('-' * 30)
        for student in students:
            print('%-5s %-15s %-3s' % (student.id, student.name, student.marks))

    def sortStudents(self, students):
        print('Sorting all student records!')
        students.sort(key=lambda student: student.marks, reverse=True)
    def deleteStudent(self, students):
        student_id = int(input("Enter student ID to delete: "))
        for student in students:
            if student.id == student_id:
                students.remove(student)
                print("Student deleted successfully.")
                return
        print("Student not found.")
    def searchStudent(self,students):
        student_id = int(input("Enter student ID to search: "))
        for student in students:
            if student.id == student_id:
                print(student)
                return
        print("Student not found.")
    def updateStudentMarks(self,students):
        student_id = int(input("Enter student ID to update: "))
        for student in students:
            if student.id == student_id:
                student.marks = int(input("Enter new marks: "))
                print("Marks updated successfully.")
                return
        print("Student not found.")
        


class Menu:
    def __init__(self, students):
        self.students = students
        self.operations = StudentOperations()

    def run(self):
        while True:
            print('\n1. Create a new student')
            print('2. List all students')
            print('3. Sort students')
            print('4. Delete the student')
            print('5. Search the student')
            print('6. Update the Students Marks')
            print('7. Exit')
            choice = int(input('Enter your choice: '))

            if choice == 1:
                self.operations.createStudent(self.students)
            elif choice == 2:
                self.operations.listStudent(self.students)
            elif choice == 3:
                self.operations.sortStudents(self.students)
            elif choice == 4:
                self.operations.deleteStudent(self.students)
            elif choice ==5:
                self.operations.searchStudent(self.students)
            elif choice ==6: 
                self.operations.updateStudentMarks(self.students)
            elif choice ==7:
                break
            else:
                print('Invalid choice!')


def StartApp():
    students = []
    menu = Menu(students)
    menu.run()


StartApp()
