
def mergeDict(x, y):\
    # since **x is put as the second argument, so if there is a same key 
    # in both dictionary, the one in x will be prioritized
    return{**y,**x} 



if __name__ == '__main__':
    x = {"a": 1, "b": 2}
    y = {"b": 3, "c": 4}
    z = mergeDict(x,y)
    print(f"z = {z}")

