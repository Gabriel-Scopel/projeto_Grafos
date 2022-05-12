from ast import NotIn
print()
lista=[]
aresmult=[]
laço=[]
count=0
grau=[]
x=0
mesmoGr=[]
completo=["O grafo é completo. Pois apresenta seu número máximo de arestas possíveis."]
regular=["O grafo não é regular. Pois todos seus vértices diferentes valores de grau."]
t_arestas=0
bi_p_comp=["O grafo não é bipartido completo. Pois as exigências para ser considerado bipartido completo não é atendida. Para isso, o grafo deve além de ser bipartido, ou seja, seus vértices podem ser dividos em dois conjuntos disjuntos X e Y tais que toda aresta conecta um vértice em X a um vértice em Y, ou seja, X e Y são conjuntos independentes, e completo, ou seja, possui o número máximo de arestas possível, sem deixar de ser bipartido."]

arq = open('A.txt', 'r')

for i in arq.readlines():
    lista.append(i.strip().split(" "))

for i in lista:
    for j in i:
        mesmoGr.append(j)
        if len(mesmoGr)!=len(grau):
            regular[0]="O grafo é regular, pois seus vértices possuem mesmo grau."
            
print(regular[0]) 

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
            completo[0]="O grafo não é completo, pois não apresenta seu número máximo de arestas possíveis."


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
else:
   print("O grafo é simples, pois não apresenta aresta multipla ou laço.")
print()
print("A sequência dos graus é:",end=" ")
for i in range(len(grau)):
    print(grau[i], end=" ")
print()

print()
print("O total de arestas é: %d" %(x/2))
print()
print(completo[0])
print()
print(regular[0])
print()


  
x = [0]
y = []
bipar = True

for linha in range(len(lista)):
	for coluna in range(len(lista)):
		if linha in x and int(lista[linha][coluna]) != 0 and coluna not in y:
			if coluna in x:
				bipar = False
			else:
				y.append(coluna)
		elif linha in y and int(lista[linha][coluna]) != 0 and coluna not in x:
			if coluna in y:
				bipar = False
			else:
					x.append(coluna)

if bipar:
	print("O grafo é bipartido, pois é possivel dividir os vértices em dois conjuntos disjuntos U e V tais que toda aresta conecta um vértice em U a um vértice em V; ou seja, U e V são conjuntos independentes.")
print()
if bipar:
    print("Bipartição: ")
    print("X={", end="")
    for v in x:
        if v==x[-1]:
            print("v{0}".format(v+1),end="}\n")
        else:
            print("v{0}".format(v+1),end=", ")
    print("Y={", end="")
    for v in y:
        if v==y[-1]:
            print("v{0}".format(v+1),end="}\n")
        else:
            print("v{0}".format(v+1),end=", ")
else:	

	print("O grafo não é bipartido, pois não é possível dividir os vértices em dois conjuntos disjuntos U e V tais que toda aresta conecta um vértice em U a um vértice em V; ou seja, U e V são conjuntos independentes.")

print()


if aresmult or laço:
    print("Não é bipartido completo, pois não é simples")
elif bipar==True:
    print("É bipartido completo, uma vez que ao dividirmos seus vértices em dois conjuntos, cada vértice de um conjunto se conecta a todos os vértices do outro conjunto.")

else:
    print("fail.")