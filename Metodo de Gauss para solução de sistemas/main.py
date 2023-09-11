from triangulamento import triangulamento
from pivotamento import pivotamento

n = int(input("Insira o número de equações "))
vetor = [] 
for i in range(1, n+1):
  temp = []
  for j in range(1, n+2):
    temp = temp + [float(input("Insira o " + str(j) + " elemento da " + str(i) + " linha "))]
  vetor = vetor + [temp]
print(vetor)
triangulamento(vetor, n)
print(vetor)
pivotamento(vetor,n) 