#4-10
place = ['beijing', 'xian', 'luoyang', 'kaifeng', 'anyang', 'nanjing', 'hangzhou']
print('The first three cities in the list are:')
print(place[:3])

print('Three cities from the middle of the list are:')
print(place[2:5])

print('The first three cities in the list are:')
print(place[-3:])

#4-11
famous_city = place[:]
place.append('shanghai')
famous_city.append('shenzhen')

print('interesting places:')
for i in place:
    print(i)

print('famous cities in China:')
for i in famous_city:
    print(i)