def mergeDict(x, y):
    return {**y, **x} # since I put **x as a second argument, so if there is a same key in both dict, then the one in x will be used. \ is continue line


if __name__ == '__main__':

    x = {"a":1, "b": 2}
    y = {"b": 3, "c": 4}
    z = mergeDict(x, y)
    print(f"z = {z}")