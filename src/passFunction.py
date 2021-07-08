"""
Pass a function to another functions as argument

so-called functional programming: focus on goals
OOP (Object Oriented Programming): focus on object
"""

def add(x, y):
    return x + y

def mul(x, y):
    return x * y

def ff(f, x, y): # ff() function is the goal, how do you do it rely on f.
    return f(x, y)

if __name__ == '__main__':
    x = add(4, 5)
    print(x)
    x = ff(add, 4, 5) # call ff()
    print(x)
    x = ff(mul, 4, 5) # call the same function ff()
    print(x)
    
    # ❓why we call ff() instead of call add() or mul() directly?
    # assignSeat(function, passengers, availableSeats) # assignSeat is a goal
