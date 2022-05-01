
lista=[]

arq = open('A.txt', 'r')

for i in arq.readlines():
    lista.append(i.strip().split(" "))


for i in range(0,11):
    for j in range(0,11):
        if i==j and lista[i][j] != '0':
            print("laço presente no vértice:", i+1)
            