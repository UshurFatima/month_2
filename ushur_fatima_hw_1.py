class Person:
    def __init__(self, fullname, age, is_married):
        self.fullname = fullname
        self.age = age
        self.is_married = is_married

    def introduce_myself(self):
        print(f"Fullname: {self.fullname} Age: {self.age} "
              f"Is_married: {self.is_married}")


class Student(Person):
    def __init__(self, fullname, age, is_married, marks):
        super().__init__(fullname, age, is_married)
        self.marks = marks

    def average_mark(self):
        print(sum(self.marks.values()) / len(self.marks))


class Teacher(Person):
    base_salary = 30000

    def __init__(self, fullname, age, is_married, experience):
        super().__init__(fullname, age, is_married)
        self.experience = experience

    def individual_salary(self, salary=base_salary):
        while self.experience > 3:
            salary += salary // 100 * 5
            self.experience -= 1
        print(f"Teacher named {self.fullname} receives {salary} "
              f"soms every month")


Math_Teacher = Teacher("Roza Daku", 33, "yes", 9)
Math_Teacher.introduce_myself()
print(f"{Math_Teacher.fullname} has been teaching for {Math_Teacher.experience} years")
Math_Teacher.individual_salary()


def create_students():
    stud1 = Student("Azamat Akjolov", 17, "no",
                    marks={
                        "Russian": 5,
                        "English": 4,
                        "Math": 4,
                        "History": 4
                    })
    stud2 = Student("Aisha Dzhusupova", 15, "no",
                    marks={
                        "Physics": 5,
                        "Chemistry": 5,
                        "Biology": 5,
                        "Geography": 4,
                        "Turkish": 4
                    })
    stud3 = Student("Nurayim Kubatova", 16, "no",
                    marks={
                        "Math": 4,
                        "Chemistry": 5,
                        "Biology": 5,
                        "History": 5,
                        "Russian": 4,
                        "English": 5
                    })
    return [stud1, stud2, stud3]


for student in create_students():
    student.introduce_myself()
    print(student.marks)
    student.average_mark()
