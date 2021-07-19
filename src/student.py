from person import *

class Student(Person): # Student inherits from Person
    def setStudentID(self, id):
        self.studentID = id # instance level attribute
    
    def __repr__(self):
        return f"{self.name}({self.studentID})"

if __name__ == '__main__':
    s = Student("John",13, "111-22-1234",'male')
    s.setStudentID("123-4566")
    print(s)
    print(s.studentID)