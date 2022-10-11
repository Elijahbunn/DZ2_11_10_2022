from re import I


number = int(input('Enter number: '))
product = 1
i = 1
dict = {}
while i <= number:
    product *= (i)
    dict[i] = product
    i += 1
print(dict)
