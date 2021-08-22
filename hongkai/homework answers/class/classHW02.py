"""
Write a Python class which has two methods get_String and print_String.
 get_String accept a string from the user 
 and print_String print the string in upper case.

Expected output:

Please enter a string: this is a test.
THIS IS A TEST.
"""

class StoreString:
    def __init__(self):
        self.storedString = ""

    def get_String(self):
        self.storedString = input("Please enter a string: ")
    
    def print_String(self):
        print(self.storedString.upper())
    
if __name__ == '__main__':
    store1 = StoreString()
    store1.get_String()
    store1.print_String()