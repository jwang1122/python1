locations = {
    "scrowdriver": "shelf1, row2, column3",
    "pliers":"shelf2, row1, column1",
    "circle-saw":"garage shelf, bottom",
    "battery":"Kitchen drawer 1",
}
a = input("Please enter the stuff you are looking for: ")

location = locations.get(a, "the stuff you are looking for is not in Database.")
print(location)