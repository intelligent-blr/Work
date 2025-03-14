class Person:
    def __init__(self, first_name, last_name, age):
        print(f"Инициализатор Person для {self.__class__}")
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.pass_id = 0

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_info(self):
        return f"Name: {self.get_full_name()}, Age: {self.age}"


class Employee(Person):
    def __init__(self, first_name, last_name, age, employee_id, position):
        # Person.__init__(self, first_name, last_name, age)
        super().__init__(first_name, last_name, age)
        self.employee_id = employee_id
        self.position = position

    def get_employee_info(self):
        basic_info = self.get_info()
        return f"{basic_info}, Employee ID: {self.employee_id}, Position: {self.position}"


class Student(Person):
    def __init__(self, first_name, last_name, age, student_id, major):
        # Person.__init__(self, first_name, last_name, age)
        super().__init__(first_name, last_name, age)
        print(f"Инициализатор Student")
        self.student_id = student_id
        self.major = major

    def get_student_info(self):
        basic_info = self.get_info()
        return f"{basic_info}, Student ID: {self.student_id}, Major: {self.major}"


emp = Employee("John", "Doe", 30, 179, "Junior MLE")
print(emp.get_employee_info())
print(emp.pass_id)

student = Student("Jane", "Smith", 20, "S54321", "Computer Science")
print(student.get_student_info())
print(student.get_info())
