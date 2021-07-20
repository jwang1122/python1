def func1(*args):
    print(f"func1{args}")
    for i in args:
        print(i)

if __name__ == '__main__':
    func1(20, 40, 60)
    print()
    func1(80, 100, 'hello', 'john', (1,2,3), ["h", "j"])