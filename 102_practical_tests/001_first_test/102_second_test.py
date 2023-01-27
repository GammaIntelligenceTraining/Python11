import math
side_a, side_b = input('Please enter two triangle sides separated by coma: ').split(', ')

print(((float(side_a) ** 2) + (float(side_b) ** 2)) ** 0.5)
print(math.sqrt(int(side_a ** 2) + (int(side_b) ** 2)))