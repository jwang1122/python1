"""
* define a dictionary, with item-location pair, find location of your item.

for example:

locations = {
    "scrowdriver": "shelf1, row2, column3",
    "pliers":"shelf2, row1, column1",
    "circle-saw":"garage shelf, bottom",
    "battery":"Kitchen drawer 1",
}

expected output:

```
Please enter the stuff you are looking for: pliers

pliers: located at shelf2, row1, column1.
```
"""

locations = {
    "scrowdriver": "shelf1, row2, column3",
    "pliers": "shelf2, row1, column1",
    "circle-saw": "garage shelf, bottom",
    "battery": "Kitchen drawer 1",
}
findThisItem = input("Please enter the stuff you are looking for: ")
print(locations.get(findThisItem))
# get(self, key, default=None, /)
