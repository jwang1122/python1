"""
* Create a new dictionay called vehicle which holds the keys: model, make, year and mileage, fill in the values of your choice.
  - Print the year of vehicle
  - Change the year to a different year
  - Add a new key called type, fill in the value (car, truck, etc)
  - Print the dictionary
"""
vehicle = {
    'Model':'Cameray',
    'Make':'Toyota',
    'Year': 2019,
    'Mileage':23
}
print(vehicle['Year'])
vehicle['Year'] = 6969
print(vehicle['Year'])

vehicle['type'] = 'car'
print(vehicle)
