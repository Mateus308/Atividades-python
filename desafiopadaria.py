int(input("opcao=0, frances= 0, integral= 0, doceLiso= 0, doceFarofa= 0, paoForma= 0 "))
float(input("valorFrances= 0, valorIntegral= 0, valorDoceLiso= 0, valorDoceFarofa= 0, valorForma= 0, valortotal"))
while (opcao !=6):
 print ("PADARIA")
 print ("[1] Pão Frances")
 print ("[2] Pão Integral")
 print ("[3] Pão Doce Liso")
 print ("[4] Pão Doce Farofa")
 print ("[5] Pão de Forma")
 print ("Fim da compra")
 opcao = (input("Escolha sua opção: "))
 while (opcao):
    opcao ==1
    print ("Digite a quantidade de pão francês que você quer: ")
    valorFrances = "frances"* 1.04
    ValorFrances = "Matematica.arredondar" (valorFrances, 2)
    break
    opcao ==2
    print ("Digite a quantidade de pão integral que você quer: ")
    valorIntegral = "integral"* 1.04
    valorIntegral = "Matematica.arredondar" (valorIntegral, 2)
    break
    opcao ==3
    print ("Digite a quantidade de pão doce liso que você quer: ")
    valorDoceLiso = "doceLiso"* 1.08
    valorDoceLiso = "Matematica.arredondar" (valorDoceLiso, 2)
    break
    opcao ==4
    print ("Digite a quantidade de pão doce farofa que você quer: ")
    valorDoceFarofa = "doceFarofa"* 1.11
    valorDoceFarofa = "Matematica.arredondar" (valorDoceFarofa, 2)
    break
    opcao ==5
    print ("Digite a quantidade de pão de forma que você quer: ")
    valorForma = "paoForma"* 0.95
    valorForma = "Matematica.arredondar" (valorForma, 2)
    break
    opcao ==6
    valortotal = (valorFrances + valorIntegral + valorDoceLiso + valorDoceFarofa + valorForma)
    valortotal = "Matematica.arredondar" (valortotal, 2)
    break
    if(frances>0):
        escreva ("\nPão Francês - Quantidade: ", frances, "| Valor: R$ ", valorFrances)
    if (integral>0):
      escreva ("Pão Integral - Quantidade: ", integral, "| Valor: R$ ", valorIntegral)
    if (doceLiso>0):
      escreva ("Pão Doce Liso - Quantidade: ", doceLiso, "| Valor: R$ ", valorDoceLiso)
    if (doceFarofa>0):
      escreva ("Pão Doce Farofa - Quantidade: ", doceFarofa, "| Valor: R$ ", valorDoceFarofa)
    if (paoForma>0):
      escreva ("Pão de Forma- Quantidade: ", paoForma, "| Valor: R$ ", valorForma)
      escreva ("Valor total da compra: R$ ", valortotal)