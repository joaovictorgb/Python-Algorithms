#Criando vetor
def cria_vetor(dimensao):
  vetor=[]
  vetor = [0]*dimensao
  return vetor
#Lendo Vetor
def ler_vetor(vetor,dimensao):
  for i in range(dimensao):
    print('Qual o valor da posição',i+1,':')
    vetor[i] = int(input(''))
  return vetor

def maior_vetor(vetor,dimensao):
  maior = vetor[0]
  pos = 0
  for i in range(dimensao):
    if vetor[i] > maior:
      maior = vetor[i]
      pos = i
  return pos

#Pedindo ao usuário a dimensão
dimensao = int(input('Qual a dimensão do vetor:'))

vetor = cria_vetor(dimensao)
vetor = ler_vetor(vetor,dimensao)
maior = maior_vetor(vetor,dimensao)

print('O maior valor está na posição',maior)
