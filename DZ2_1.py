number = str(input('Enter number: '))
number = number.replace(',', '')
number = number.replace('.', '')
list = []
i = 0
sum = 0
while i < len(number):
    list.append(int(number[i]))
    i += 1

print(list)

for i in range(len(list)):
    sum += list[i]

print(sum)
