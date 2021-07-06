for i in range(10):
    if (i % 2 == 1):
        print(i)

input = input("Please enter a test string: ")
if len(input) < 5:
    print("Your string is too short.")
    print("Please enter a string with at least 5 characters.")

print("Done.")


