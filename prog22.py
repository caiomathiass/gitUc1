dia = input("Digite o dia da semana")
match dia:
    case "segunda"|"terça"|"quarta"|"quinta"|"sexta":
     print ("Dia de semana. Dia de programar!") 
    case "sabado"|"domingo":
      print("Fim de semana! Hora de descansar.")
    case _: 
     print("Dia invalido.")