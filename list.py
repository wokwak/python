garage=['toyota','honda','izusu']
garage.append('suzuki')
#print(garage[2])
garage.remove('honda')
garage.insert(1,'kawasaki')
del garage[2]
#print(garage[-1])
#print(garage[-2])
mycar = garage.pop(-1)
print(mycar)
garage.append('suzuki')
garage.append('izusu')
garage.append('zzzzz')
print(garage)
garage[-1]='tesla'
print(len(garage))
garage.sort()
garage.sort(reverse=True)
print(sorted(garage))
print(garage)
garage.reverse()
print(garage)
for u in garage:
    print('hello',u)
    print('hello'+u)

