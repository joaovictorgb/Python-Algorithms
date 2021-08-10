#Jogo do imprensadinho 
print('-----Seja Bem vindo ao jogo do imprensadinho!----- ')
#chamar números aleatórios 
import random
numgerator= random.randint(2,99)
#primeira variavel e resposta do usúario
primeiro = 2 
ultimo = 99
user = int(input('Digite um número que esteja entre 2 a 99:  '))
#regras if e elif
if user > numgerator:
   ultimo = user
elif user < numgerator :
    primeiro = user
#Agora a segunda chamada de usuario,,só que com while ,if e else
while user != numgerator and (ultimo != numgerator+1 or primeiro != numgerator-1) :
   if user >numgerator: 
            print('Tente novamente,só que agora entre' ,primeiro, "e", user)
            user= int(input(''))
            if user > numgerator:
               ultimo= user
            else:
                primeiro= user 
#Segunda chamada de usuario com if,elif
   else:
       if user< numgerator :
         print('Tente novamente,só que agora entre',user, 'e',ultimo)
         user = int(input(''))
         if user >numgerator :
            ultimo = user
         elif user < numgerator :
            primeiro = user
#O usúario irá ganhar se :
if ultimo == numgerator+1 and primeiro == primeiro-1 and user != numgerator :
    print("Congratulações ! O número final é",numgerator," 🎉🥳👏" )
#em caso de derrota vai retornar ao usuario a seguinte mensagem!
elif user == numgerator:
  print("Não foi desta vez! o número é ",numgerator,"😰")
