class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def introduce(self):
        print(f"Hello, my name is {self.name}.")
        print(f"I am {self.age} years old.")
        print(f"I am studying {self.course}.")


student1 = Student("Kendra", 20, "Information Technology")
student2 = Student("Rizza", 21, "Tourism")
student3 = Student("lily", 23, "Philosophy")


student1.introduce()
print()  
student2.introduce()
print() 
student3.introduce()