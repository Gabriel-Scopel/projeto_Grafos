
lista=[]

arq = open('A.txt', 'r')

for i in arq.readlines():
    
        lista.append(i.strip().split(" "))
        
    #lista.append(i.strip())

print(lista)

