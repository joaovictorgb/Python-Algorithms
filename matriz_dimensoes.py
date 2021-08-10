#Crianção da matriz 
def criacao_matriz(linhas,colunas):
  matriz = []
  for i in range(linhas):
    matriz.append([0]* colunas)
  return matriz
#Lendo a Matriz
def lendo_matriz(matriz,linhas,colunas):
  for i in range(linhas):
    for j in range(colunas):
      print('Qual a  posição da linha',i+1,'e da coluna',j+1)
      matriz[i][j] = int(input(''))
  return matriz

def maior_matriz (matriz,linhas,colunas):
  maior = matriz[0][0]
  l = 0 
  c = 0
  for i in range(linhas):
    for j in range(colunas):
      if matriz[i][j] > maior:
        maior = matriz[i][j]
        l = i
        c = j
  return l,c
#usuário resposta
linhas = int(input('Digite o quantidade de linhas:'))
colunas = int(input('Digite o quantidade de colunas:'))

matriz1 = criacao_matriz(linhas,colunas)

matriz1 = lendo_matriz(matriz1,linhas,colunas)

print('O termo maior está na posição',maior_matriz(matriz1,linhas,colunas))
