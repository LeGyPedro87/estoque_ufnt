
tipoA = [3,5,7]
tipoB = [6,7,9]
tipoC = [9,5,4]
tipoD = [1,6,7]

loja = []

loja.append(tipoA)
loja.append(tipoB)
loja.append(tipoC)
loja.append(tipoD)

#vizu todos
print("\nEstoque inicial:")
for i in range(len(loja)):
  print(loja[i])

#interface
while True:
  print("\n ======= LOJA =======")
  print("[1] - Consultar um Modelo")
  print("[2] - Adicionar Itens")
  print("[3] - RemoveR Itens")
  print("[0] - Sair")

  opc = int(input("\nDigite qual opção deseja: "))

  if (opc == 1): # ver modelo

    tipo = (input("\nTipo de camisa:(A/B/C/D): ")).upper()
    if(tipo == "A"):
      tipo = 0
    elif (tipo == "B"):
      tipo = 1
    elif(tipo == "C"):
      tipo = 2
    elif(tipo == "D"):
      tipo = 3
    else:
      raise ValueError("Valor inválido")

    tamanho = (input("Qual Tamanho(P/M/G): ")).upper()
    if tamanho == "P":
      tamanho = 0
    elif(tamanho == "M"):
      tamanho = 1
    elif(tamanho == "G"):
      tamanho = 2
    else:
      raise ValueError("Valor invalido!")

    print(f"\nQuantidade Disponivel:{loja[tipo][tamanho]}")

  elif(opc == 2): # adiciona ao estoque

    tipo = (input("Tipo de camisa(A/B/C/D): ")).upper()
    if(tipo == "A"):
      tipo = 0
    elif (tipo == "B"):
      tipo = 1
    elif(tipo == "C"):
      tipo = 2
    elif(tipo == "D"):
      tipo = 3
    else:
      raise ValueError("Valor inválido")

    tamanho = (input("Qual Tamanho(P/M/G): ")).upper()
    if tamanho == "P":
      tamanho = 0
    elif(tamanho == "M"):
      tamanho = 1
    elif(tamanho == "G"):
      tamanho = 2
    else:
      raise ValueError("Valor invalido!")

    quantidade = int(input("Quantidade a Adicionar: "))

    if quantidade <= 0:
      raise ValueError("Quantidade inválida!")

    loja[tipo][tamanho] += quantidade

    # vizu depois da adição
    print(f"\nNovo valor: {loja[tipo][tamanho]}\n")

    for i in range(len(loja)):
     print(loja[i])

  elif (opc == 3): # remover

    tipo = (input("\nTipo de Camisa(A/B/C/D): ")).upper()
    if(tipo == "A"):
      tipo = 0
    elif (tipo == "B"):
     tipo = 1
    elif(tipo == "C"):
      tipo = 2
    elif(tipo == "D"):
      tipo = 3
    else:
      raise ValueError("Valor inválido")

    tamanho = (input("Qual Tamanho(P/M/G): ")).upper()
    if tamanho == "P":
      tamanho = 0
    elif(tamanho == "M"):
     tamanho = 1
    elif(tamanho == "G"):
      tamanho = 2
    else:
      raise ValueError("Valor invalido!")

    quantidade = int(input("Quantidade a Remover:"))
    disponivel = loja[tipo][tamanho]

    if (quantidade <= 0):
      raise ValueError("Quantidade inválida!")

    if (quantidade > disponivel): #verificação
      raise ValueError("Quantidade de peças não pode ser maior que a Disponivel!")

    loja[tipo][tamanho] -= quantidade

    #vizu depois da remoção
    for i in range(len(loja)):
      print(loja[i])

  elif(opc == 0): # Sair
    print("\nVolte Sempre!")

    for i in range(len(loja)):
      print(loja[i])

    break

  else:
    print("\nOpção Inválida!, Tente Novamente!")
    