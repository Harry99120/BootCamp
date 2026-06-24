class Student:
    count = 0

    def __init__(self, roll_no, marks):
        self.__roll_no = roll_no
        self.__marks = marks
        self._grade = "N/A"
        Student.count += 1

    @property
    def gpa(self):
        return sum(self.__marks) / len(self.__marks) / 10

    @gpa.setter
    def gpa(self, marks):
        if 0 <= marks <= 100:
            self.__marks = marks
        else:
            print("Invalid marks")

# Example
s1 = Student(1, [80, 90, 95])
print(f"GPA: {s1.gpa}, Total Students: {Student.count}")