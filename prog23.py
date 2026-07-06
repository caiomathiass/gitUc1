erro = int(input("codigos de erro, digite o codigo de erro: "))
match erro:
  case 200:
    print("Sucesso! Tudo certo com a sua requisição.")
  case 400:
    print("Erro do cliente: Requisição malformada.")
  case 401|403: 
    print(" Erro de permissão: voce nao tem acesso a esta pagina.")
  case  404:
    print ("Erro: Pagina não encontrada.")
  case 500|503:
    print("Erro no servidor: Nosso sistema está instável no momento.")
  case _:
    print("Codigo HTTP {codigo_status} desconhecido")
