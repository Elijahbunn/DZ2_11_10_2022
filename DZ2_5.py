number = int(input('Enter length of list: '))
list = []
i = 0
while i < number:
    list.append(int(input(f'Enter number {i+1}: ')))
    i += 1
print(f'Prime list: {list}')

i = 0
while i < (number/2):
    tmp = list[i]
    list[i] = list[number - 1 - i]
    list[number - 1 - i] = tmp
    i += 1
print(f'Second list: {list}')
