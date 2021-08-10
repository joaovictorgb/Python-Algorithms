#Quantidades
Linhas = 10 ; Colunas = 2 ; mtimes = [] ;mplacar = [] ; vencedores = [] 
#Gerando as matrizes dos times e do placar
for i in range(Linhas):
  mtimes.append([0] * Colunas)
for i in range (Linhas):
   mplacar.append([0] * Colunas)
#Adiçao dos times e do placar
for i in range(Linhas):
     for b in range (Colunas):
       print('Digite os times que se enfrentaram', i+1, ':',end ='')
       mtimes[i][b] =input('')
     print()
for i in range(Linhas):
     for b in range (Colunas):
       print('Digite o placar da partida', i+1, ':',end ='')
       mplacar[i][b] =int(input())
     print()
#Laço verificador
for i in range(Linhas):
    if mplacar[i][0] > mplacar[i][1] :
       vencedores.append(mtimes[i][0])
       
    elif mplacar[i][0] < mplacar[i][1]:
         vencedores.append(mtimes[i][1])
         
#Condicionais para respostas de usuário 
if len(vencedores) == 0:
  print('Todos os jogos empataram')
else:
  print('Times que ganharam:', end = '')
  for t in range(len(vencedores) -1):
      print(vencedores[t] , end = '-')
  print(vencedores[t + 1])
