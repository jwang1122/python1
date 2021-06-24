x = input("Enter a file name with extension: ")

index = x.index('.')
ext = x[index:]
print(f"The extension of the file named '{x}' is '{ext}'.")