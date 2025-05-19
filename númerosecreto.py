#Declarar variáveis
import random
numero_secreto = random. randint (1,10)
tentativas =0
contagem_tentativas = 0
# laço de repetição
while tentativas != numero_secreto:
    numero = int(input("Digite um número: "))
    contagem_tentativas= contagem_tentativas+1
    if numero == numero_secreto:
        break
    elif numero < numero_secreto:
        print ("O número secreto é maior.")
    else:
        print ("O número secreto é menor.")