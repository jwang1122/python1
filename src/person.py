class Person:
    def __init__(self, name, age, ssn, gender):
        self.name = name
        self.age = age
        self.ssn = ssn
        self.gender = gender

    def __repr__(self):
        return f"{self.name}({self.ssn}, {self.age}, {self.gender})"

if __name__ == '__main__':
    p1 = Person("Kayden", 11, "246-69-1357", 1)
    print(p1)