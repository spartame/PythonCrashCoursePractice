#4-1
#beijing, xian, luoyang, kaifeng, anyang, nanjing, hangzhou

place = ['beijing', 'xian', 'luoyang', 'kaifeng', 'anyang', 'nanjing', 'hangzhou']

for visit in place:
    print(visit.title() + ' is not a beautiful city')
    
print('cities all the same, boring and lame')

#4_2
for value in range(1, 6):
    print('\n' + str(value))
    
squares = []
for value in range(1, 11):
    #square = value ** 2
    squares.append(value ** 2)

print(squares)    

