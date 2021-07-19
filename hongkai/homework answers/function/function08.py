"""
* Write a function func1() such that it can accept a variable length of argument and print all arguments value

func1(20, 40, 60)
func1(80, 100)

Expected Output:
func1(20, 40, 60)
20
40
60

func1(80, 100)
80
100
"""

def func1(*args):
    print("func1", args, sep="")
    for i in args:
        print(i)

if __name__ == '__main__':
    func1(20, 40, 60)
    func1(80, 100)