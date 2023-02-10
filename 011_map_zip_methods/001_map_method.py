# map() method is used to iter through functions
def func(x):
    return x ** x

int_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Long way
new_list = []
for x in int_list:
    new_list.append(func(x))

print(new_list)

# Using map()
print(map(func, int_list))
print(list(map(func, int_list)))


# List comprehension
print([func(x) for x in int_list])
print([func(x) for x in int_list if x % 2 == 0])


cars = [
    {
        'make': 'Merceds',
        'model': 'S500',
        'color': 'black'
    },
    {
        'make': 'Bmw',
        'model': 'M5',
        'color': 'red'
    },
    {
        'make': 'Audi',
        'model': 'A7',
        'color': 'white'
    }
]

def return_dictionary(car):
    make, model, color = car['make'], car['model'], car['color']
    return {
        color: {
            'make': make,
            'model': model
        }
    }

new = map(return_dictionary, cars)
for color in new:
    print(color)

print(cars)



