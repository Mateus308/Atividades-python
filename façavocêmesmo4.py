opcao = 5
while opcao !=5:
    print ("--- Calculadora ---")
    print ("0. +")
    print ("1. -")
    print ("2. *")
    print ("3. /")
    print ("4. Sair")
    opcao = (input("Escolha uma opção: "))
    if opcao ==0:
        print ("Você escolheu +.")
    elif opcao ==1:
        print ("Você escolheu -.")
    elif opcao ==2:
        print ("Você escolheu *.") 
    elif opcao ==3:
        print ("Você escolheu /.")
    elif opcao ==4:
        print ("Você escolheu Sair.")
    break 
else:
    print ("Opção inválida. Tente novamente")             