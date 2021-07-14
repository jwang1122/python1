from person import *

class Student(Person): # student inherits from Person
    def setStudentID(self, id):
        self.studentID = id # instance level attribute

    def __repr__(self):
        return f"{self.name}({self.studentID})"

if __name__ == '__main__':
    s = Student("Kayden Jr.", 11, "123-45-6789", 'male')
    s.setStudentID("135-2468")
    print(s)
    print(s.studentID)