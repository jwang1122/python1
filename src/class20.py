"""
Inner or Nested Classes

"""

class Outer:
    class Inner:
        pass
        class InnerOfInner:
            pass

    class _Inner:
        pass

if __name__ == '__main__':
    print(dir(Outer))
    print(type(Outer.Inner()))