
list = ['Giao','Master of Shadow','Jumo','Kunkun']

print("Invitation list:" + str(list))
list[2] = 'Black'
print("Invitation list:" + str(list))
list.insert(0,'huohua')
print("Invitation list:" + str(list))
list.append('Jumo')
print("Invitation list:" + str(list))

for i in range(len(list)-2):
    list.pop()
    print("Invitation list:" + str(list))
for i in range(2):
    del list[0]
    print("Invitation list:" + str(list))
