c = 4;
while c!=0:
    print(c)
    if c==2:
        print('On y est presque')
    c -=1
    if c==0:
        print('c\'est bon')




nom = None

while nom!='prince':
    nom = input('> Entre un nom : \n')
    print(nom)
    if nom=='prince':
        print('Well done.')
    break
