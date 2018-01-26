names = ['zhang3', 'li4', 'wang5']
print(names)
#3-1
print(names[-3])
print(names[-2])
print(names[-1])
#3-2
print('nice to meet you, dear ' + names[0])
print('nice to meet you, dear ' + names[1])
print('nice to meet you, dear ' + names[2])
#3-5
print(names[0] + ' can not show up')
names[0] = 'zhao6'
print(names[0] + ', welcome!')
print(names[1] + ', welcome!')
print(names[2] + ', welcome!')
#3-6
print('find a bigger table!')
names.insert(0, 'charu1')
names.insert(2, 'charu2')
names.append('charu3')
print(names[0] + ', welcome!')
print(names[1] + ', welcome!')
print(names[2] + ', welcome!')
print(names[3] + ', welcome!')
print(names[4] + ', welcome!')
print(names[5] + ', welcome!')
#3-7
print('we can invite only two guests now,sorry')
delGuests = names.pop()
print(delGuests + ", kick you out.")
delGuests = names.pop()
print(delGuests + ", kick you out.")
delGuests = names.pop()
print(delGuests + ", kick you out.")
delGuests = names.pop()
print(delGuests + ", kick you out.")
print("welcome, " + names[0])
print("welcome, " + names[1])
del names[0]
del names[0]
print(names)