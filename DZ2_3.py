number = int(input('Enter number: '))
i = 1
sum = 0
dict = {}
dict2 = {}
while i <= number:
    product = round((1 + 1/i)**i, 2)
    sum += product
    dict[i] = product
    dict2[i] = sum
    i += 1
print(f'Последовательность до {number}: {dict}')
print(f'Список сумм: {dict2}')
