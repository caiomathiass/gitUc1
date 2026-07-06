print("Seja bem-vindo ao exercito Brasileiro ")
gen = input("Digite seu genero M ou F" ).upper()
ida = int(input("Qual sua idade?" ))
if gen == "M" and ida >= 18:
    print("Apto a se candidatar")
else:
    print("Não, apto")
