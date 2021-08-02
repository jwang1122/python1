"""
* Write a Python class named Student with two attributes student_id, student_name. 
Add a new attribute student_class and display the entire attribute and their values of the said class. 
Now remove the student_name attribute and display the entire attribute with values.

Expected output:

```
Original attributes and their values of the Student class:
student_id -> V10
student_name -> Jacqueline Barnett

After adding the student_class, attributes and their values with the said class:
student_id -> V10
student_name -> Jacqueline Barnett
student_class -> V

After removing the student_name, attributes and their values from the said class:        
student_id -> V10
student_class -> V
```
"""

class Student:
    def __init__(self, student_id, student_class):
        self.student_id = student_id
        self.student_class = student_class
    
    def __repr__(self):
        return f"({self.student_id}, {self.student_class})"

if __name__ == '__main__':
    kid = Student("V10", "V")
    print(kid)