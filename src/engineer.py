from person import *

class Engineer(Person):
    def setEmployeeID(self, id):
        self.employeeID = id

    def __repr__(self): # override __repr__()
        return f"{self.name}(Employee ID: '{self.employeeID}')"

if __name__ == '__main__':
    e1 = Engineer("John",45,"111-22-3333",'male')
    e1.setEmployeeID("E-1234")
    print(e1)