cars = ['volvo', 'bmw', 'citroen', [1, 2, 3]]
# print(cars)
# cars.append('opel')
# print(cars)
# print(cars[3][2])
# deleted = cars.pop(0)
# print(cars, deleted)
cars[0], cars[1] = cars[1], cars[0]
del cars[3]
# cars.remove('opel')
cars.sort()
cars.reverse()
print(cars)