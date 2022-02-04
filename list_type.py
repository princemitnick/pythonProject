a = []

c = 5

while c!=0:
    nom = input("> Put a name in the list : ")
    a.append(nom)
    c -=1

print(a)

for i in range(len(a)):
    print(a[i])
