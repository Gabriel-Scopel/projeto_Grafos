
lista=[]
aresmult=[]
laço=[]
count=0
grau=[]

arq = open('A.txt', 'r')

for i in arq.readlines():
    lista.append(i.strip().split(" "))


for i in lista:
    somagr=0
    for j in i:
        if j != '':
            somagr+=int(j)
    grau.append(somagr)


for i in range(0,11):
    somagr=0
    for j in range(0,11):
        somagr+=int(lista[i][j])
        if(int(lista[i][j]) > 1):
            aresmult.append(i+1)
            aresmult.append(j+1)
            count+=1
    
        if i==j and lista[i][j] != '0':
            laço.append(i+1)
    
 
            

if aresmult[0] or laço[0]:
    for i in range(int(count/2)):
        print("Aresta multipla presente entre os vértices V",aresmult[i], "e", "V",aresmult[i+1])
    for i in range(len(laço)):
        print("laço presente em:", laço[i])


print("A sequência dos graus é:",sorted(grau))
