cargo=input("Qual o cargo?  ") .upper()
if cargo == "CAIXA":
    s= 1500
elif cargo ==  "VENDEDOR":
    s= 2400
elif cargo == "GERENTE":
    s=4000
else:
    s= 0
    print("Cargo não existe, digite um cargo válido")
    inss=s * 0.12
    #irrf
    if s > 2000:
        irrf = s * 0.14
    else:
        irrf = s * 0.08
    #fim do irrf
    sf = s - irrf - inss
    print(f"Quesrido seu cargo de {caro} tem o salario de {s} e os impostos são:")
    print(f"inss -> {inss}")
    print(f"irrf -> {irrf}")
    print (f"Seu salario final é {sf}")
    