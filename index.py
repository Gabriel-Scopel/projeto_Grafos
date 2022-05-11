
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
t_arestas=0
bi_p_comp=["O grafo não é bipartido completo"]

arq = open('matriz.txt', 'r')

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


for i in range(len(lista[0])):
    somagr=0
    for j in range(len(lista[0])):
        if(int(lista[i][j])==0):
            completo[0]="O grafo não é completo"


        somagr+=int(lista[i][j])
        if(int(lista[i][j]) > 1):
            aresmult.append(i+1)
            aresmult.append(j+1)
            count+=1
    
        if i==j and lista[i][j] != '0':
            laço.append(i+1)
        
if aresmult or laço:
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


xv=[]
yv=[]
x=[]
y=[]
bipartido=["É bipartido"]

for j in range(len(lista[0])):
  if(j%2==0):
    for i in range(len(lista[0])):
        if lista[j][i]!="0":
          xv.append(i+1)
  elif(j%2!=0):
    for i in range(len(lista[0])):
      if lista[j][i]!="0":
          yv.append(i+1)

for i in xv:
  if i not in x:
    x.append(i)

for i in yv:
  if i not in y:
    y.append(i)
    
for i in x:
  for j in y:
    if(i==j):
      bipartido[0]="Grafo não é bipartido."
      
if(laço):
    bipartido[0]="Grafo não é bipartido."
print(bipartido[0])


if(bipartido[0]=="É bipartido"):
    print("Sua bipartição é: ")
    print("Vertices de um conjunto que denominamos X: ", x)
    print("Vertices de um conjunto que denominamos Y: ", y)


for i in lista:
  for j in i:
    t_arestas+=int(j)


if(len(x)*len(y)==t_arestas/2 and bipartido[0]=="É bipartido"):
  bi_p_comp[0]="O grafo é bipartido completo."

print(bi_p_comp[0])

""" 
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
t_arestas=0
bi_p_comp=["O grafo não é bipartido completo"]

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


xv=[]
yv=[]
x=[]
y=[]
bipartido=["É bipartido"]

for j in range(len(lista[0])):
  if(j%2==0):
    for i in range(len(lista[0])):
        if lista[j][i]!="0":
          xv.append(i+1)
  elif(j%2!=0):
    for i in range(len(lista[0])):
      if lista[j][i]!="0":
          yv.append(i+1)

for i in xv:
  if i not in x:
    x.append(i)

for i in yv:
  if i not in y:
    y.append(i)
    
for i in x:
  for j in y:
    if(i==j):
      bipartido[0]="Grafo não é bipartido."
      
if(laço):
    bipartido[0]="Grafo não é bipartido."
print(bipartido[0])


if(bipartido[0]=="É bipartido"):
    print("Sua bipartição é: ")
    print("Vertices de um conjunto que denominamos X: ", x)
    print("Vertices de um conjunto que denominamos Y: ", y)


for i in lista:
  for j in i:
    t_arestas+=int(j)


if(len(x)*len(y)==t_arestas/2 and bipartido[0]=="É bipartido"):
  bi_p_comp[0]="O grafo é bipartido completo."

print(bi_p_comp[0]) """


