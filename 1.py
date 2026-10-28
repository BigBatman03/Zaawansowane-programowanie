class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def ocena(self):
        if self.marks > 50:
            return True
        else:
            return False


student1 = Student("John", 75)
student2 = Student("Alice", 45)
print(student1.ocena())
print(student2.ocena())
