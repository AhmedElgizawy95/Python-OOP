class human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print(f"{self.name} says: Hello!")




class student(human):
    def __init__(self, name, age, student_id):
        human.__init__(self, name, age)
        self.student_id = student_id

    def study(self):
        print(f"{self.name} is studying.")




if __name__ == "__main__":
    person1 = human("Alice", 30)
    person1.speak()
    
    student1 = student("Bob", 20, "S12345")
    student1.speak()
    student1.study()