def triangulamento(vetor, n):
  for k in range(n-1):
    for i in range(k+1, n):
      if vetor[k][k] != 0:
        aux = vetor[i][k]/vetor[k][k]
      else:
        count = k + 1
        while (vetor[k][k] == 0):
          if (count > n):
            print("Não existe solução")
          saver = vetor[k] 
          vetor[k] = vetor[count]
          vetor[count] = saver
        aux = vetor[i][k]/vetor[k][k]
      for j in range(n+1):
        vetor[i][j] = vetor[i][j] - vetor[k][j]*aux    