opcao = int(input("Digite uma opção"))

match opcao:
case 1:
print("Voce escolheu a opção 1: Ver saldo.")
case 2: 
print(" Voce escolheu a opção 2: Fazer saque.")
case 3 :
print("Voce escolheu a opção 3: Falar com um atendente.")
case _:
print(" Opçao invalida!")