
from ast import NotIn


lista=[]
aresmult=[]
laço=[]
count=0
grau=[]
x=1
mesmoGr=[]
completo=["O grafo é completo"]
regular=["O grafo é regular"]

arq = open('A.txt', 'r')

for i in arq.readlines():
    lista.append(i.strip().split(" "))

for i in lista:
    for j in i:
        mesmoGr.append(j)
        if len(mesmoGr)!=len(grau):
            regular[0]="O grafo não é regular"
            
    

for i in lista:
    somagr=0
    for j in i:
        if j != '' and int(j)!=0:
            x+=int(j)
            somagr+=int(j)
    grau.append(somagr)


for i in range(0,11):
    somagr=0
    for j in range(0,11):
        if(int(lista[i][j])==0):
            completo[0]="O grafo não é completo"


        somagr+=int(lista[i][j])
        if(int(lista[i][j]) > 1):
            aresmult.append(i+1)
            aresmult.append(j+1)
            count+=1
    
        if i==j and lista[i][j] != '0':
            laço.append(i+1)
        
if aresmult[0] or laço[0]:
    print("O grafo não é simples, pois apresenta:")
    for i in range(int(count/2)):
        print("Aresta multipla presente entre os vértices V",aresmult[i], "e", "V",aresmult[i+1])
    print()
    for i in range(len(laço)):
        print("laço presente em:", laço[i])

print("A sequência dos graus é:",end=" ")
for i in range(len(grau)):
    print(grau[i], end=" ")
print()

print("O total de arestas é: %d" %(x/2))
print(completo[0])
print(regular[0])

