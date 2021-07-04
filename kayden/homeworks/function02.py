

def mergeDict(x, y):
     return {**y, **x}

x = {"a": 1, "b": 2}
y = {"b": 3, "c": 4}
z = mergeDict(x, y)

print(f"z = {z}")