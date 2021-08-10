valor1 = []
valor2 = []
lista = []
num = 0
#Solicite ao usuário a digitação de dois valores
qtd = int(input('Diga a quantidade de valores que irão ser digitados : '))
#Encontre no vetor a primeira instância de cada um dos dois valores digitados
#Criação da lista com o laço.
num = int(input('Digite um número inteiro: ')); lista.append(num)
for i in range(qtd-1):
  num = int(input('Digite outro número inteiro: ')); lista.append(num)
# Print com a lista.
print('Aqui está sua lista: ',lista)
#fazer a checagem.
n1 = int(input('Digite um número inteiro para ser checado na lista: '));
n2 = int(input('Digite o outro número inteiro para ser checado: '))
#primeira instancia dos numeros.
if n1 in lista :
    valor1.append(lista.index(n1))
if n2 in lista:
    valor2.append(lista.index(n2))
#Caso algum dos valores não esteja presente no vetor, imprima uma mensagem avisando ao usuário.
if valor1 and valor2:
    lista.pop(valor1[0]);lista.insert(valor1[0],n2);lista.pop(valor2[0]);lista.insert(valor2[0],n1);print('o vetor resultante é: ',lista)
else:
    print('Um dos valores não constam na lista.')
