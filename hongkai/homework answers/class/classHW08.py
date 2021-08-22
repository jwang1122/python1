"""
* Write a Python class named Student with two instances student1, 
student2 and assign given values to the said instances attributes. 
Print all the attributes of student1, student2 instances 
with their values in the given format.

Expected output:
```
student_id -> V12
student_name -> Ernesto Mendez


student_id -> V12
marks_language -> 85
marks_science -> 93
marks_math -> 95
```
"""

class Student:
    def __init__(self, id, name, scores=None):
        self.id = id
        self.name = name
        self.scores = scores
    
    def __repr__(self):
        return f"{self.name}, {self.id}"

    def displayScores(self):
        if self.scores:
            print(self.scores)

class Course:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name

if __name__ == '__main__':
    student1 = Student("V12", "Ernesto Mendez")
    print(student1)

    scores = {Course("language"):85, Course("science"):93, Course("math"):95}
    student1 = Student("V12", "Ernesto Mendez", scores)
    student1.displayScores()
