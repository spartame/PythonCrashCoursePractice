#4-3
number = []
for i in range(1, 21):
    number.append(i)
    
print(number)

#4-4, 4-5
number2 = []
for i in range(1, 100001):
    number2.append(i)
    
print(number2)
print(min(number2))
print(max(number2))
print(sum(number2))

#4-6
number3 = []
for i in range(1, 21, 2):
    number3.append(i)
for i in number3:    
    print(i)
print('\n')

#4-7
number4 = []
for i in range(3, 31, 3):
    number4.append(i)
for i in number4:    
    print(i)
print('\n')
    
#4-8
number5 = []
for i in range(1, 11):
    number5.append(i ** 3)
for i in number5:
    print(i)
print('\n')

#4-9
number6 = [i**3 for i in range(1, 11)]
print(number6)
