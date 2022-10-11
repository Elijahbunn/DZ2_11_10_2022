import random

with open('DZ2_4.txt', 'r') as dz_file:
    numbers = dz_file.read()
position = numbers.split()

number2 = int(input('Enter number: '))
list = [number2]
i = 1
while i < number2:
    list.append(random.randint((-1)*number2, number2))
    i += 1
print(f'position: {position}')
print(f'numbers: {list}')

sum = 0
l = 0
m = 0
while m < len(position):
    sum += list[int(position[m])]
    print(f'sum №{m+1}: {sum}')
    m += 1
print(f'final sum is {sum}')
