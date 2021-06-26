l1 = [10, 20, 23, 11, 17]
l2 = [13, 43, 24, 36, 12]
l3 = [n for n in l1 if n%2]+[n for n in l2 if not n%2]
print(f"result List is {l3}")