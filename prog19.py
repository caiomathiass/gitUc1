print("Acesso a Montanha ")
ing = input("Voce possui ingresso? S / N  " ).upper()
ida = int(input("Qual sua idade?" ))
if ing == "S" and ida >= 12:
    print("Acesso Liberado! Diverta-se!")
elif ing == "S" and ida <= 11:
    print("Voce tem o ingresso, mas é menor de idade.")
elif ing == "N":
    print("Acesso negado, compre um ingresso em um dos nossos caixas, obrigado")
else:
    print("Acesso negado, você precisa de um ingresso")