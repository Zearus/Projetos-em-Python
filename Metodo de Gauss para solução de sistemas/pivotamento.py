def pivotamento(vetor, n):
  resultado = []
  for i in  range(n):
    resultado = resultado + [['x' + str(i+1), 0]]
  for i in range(n-1, -1, -1):
    soma = 0
    for j in range(n-1, i, -1):
      soma = soma + vetor[i][j]*resultado[j][1]
    if vetor[i][i] == 0:
      print("O sistema não tem solução")
      return
    resultado[i][1] += (vetor[i][n]-soma)/vetor[i][i]
  print(resultado)