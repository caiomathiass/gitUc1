print("Olá seja bem vindo")
nome = input("Diga seu nome para começar")
b1 = float(input("me fale a sua nota do Primeiro bimestre"))
b2= float(input("Agora sua nota do segundo"))
b3 = float(input("diga a do terceiro"))
b4 = float(input("agora do quarto"))
m = (b1 + b2 + b3 +b4) /2
print (f"{nome} Sua média é {m}")
if m >= 6:
    print ("Aprovado")
else :
    print ("Recuperação")