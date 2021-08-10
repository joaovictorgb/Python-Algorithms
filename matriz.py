#Criando a matriz
matriz= []
def criando_matriz (dimensao_matriz):
    for i in range (dimensao_matriz):
      matriz.append([0]* dimensao_matriz )
    return matriz
#Lendo a matriz
def lendo_matriz(matriz,dimensao_matriz):
    for i in range (dimensao_matriz):
      for j in range(dimensao_matriz):
         print('Posição da linha',i+1,'da coluna',j+1)
         matriz[i][j] = int(input())
    return matriz
#Matriz transposta
def transposta(matriz,dimensao_matriz,matriz_result):
    for i in range(dimensao_matriz):
     for j in range (dimensao_matriz):
      matriz_result[i][j] = matriz=[j][i]
    return matriz_result
#Usuário informando a dimensão da Matriz
dimensao_matriz = int(input('Informe a dimensão da Matriz:'))

primeira_matriz = criando_matriz(dimensao_matriz)
primeira_matriz = lendo_matriz(primeira_matriz,dimensao_matriz)
mtransposta = criando_matriz(dimensao_matriz)
mtransposta = transposta (primeira_matriz,dimensao_matriz,mtransposta)
print(primeira_matriz)
print(mtransposta)
