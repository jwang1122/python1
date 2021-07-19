class Person:
    def __init__(self, name, age, ssn, gender):
        self.name= name # create instance level attribute
        self.age = age
        self.ssn = ssn
        self.gender = gender

    def __repr__(self):
        return f"{self.name}({self.ssn}, {self.age}, {self.gender})"

if __name__ == '__main__':
    p1 = Person("John", 12, "111-22-1234", "male")
    print(p1)