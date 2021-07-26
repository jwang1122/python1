"""
* Create a function showEmployee() in such a way that it should accept employee name, and its salary and display both. 
If the salary is missing in the function call assign default value 9000 to salary

showEmployee("Ben", 9000)
showEmployee("Ben")

Expected output:

Employee Ben salary is: 9000
Employee Ben salary is: 9000
"""

def showEmployee(name, salary = 9000):
    print(f"Employee {name} salary is: {salary}")

if __name__ == '__main__':
    showEmployee("Ben", 9000)
    showEmployee("Ben")