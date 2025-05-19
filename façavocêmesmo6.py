opcao = 3
while opcao !=3:
    print ("0. Celsius")
    print ("1. Fahrenheit")
    print ("2. Kelvin")
    opcao = (input("Escolha uma uma opção: "))
    if opcao ==0:
        print ("Você escolheu Celsius.")
    elif opcao ==1:
        print ("Você escolheu Fahrenheit.")
    elif opcao ==2:
        print ("Você escolheu Kelvin.")
    break
else:
    print ("Opção inválida. Tente novamente")