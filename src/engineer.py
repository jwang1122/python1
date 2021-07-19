from person import *

class Engineer(Person):
    def setEmployeeID(self, id):
        self.employeeID = id

    def __repr__(self): # override __reper__
        return f"{self.name}(Employee ID: '{self.employeeID}')"

if __name__ == '__main__':
    e1 = Engineer("Dude the dude", 'age: really old', "ssn: 549-353-7735", 'gender: dude')
    e1.setEmployeeID("E-5548")
    print(e1)