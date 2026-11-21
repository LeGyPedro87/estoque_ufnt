loja = [

    [3,5,7],
    [6,7,9],
    [9,5,4],
    [1,6,7]

]

for i in range(len(loja)):
  print(loja[i])

def tipo(): # tipo
    tipo = input("\nSelecione o Tipo(A/B/C/D): ").upper()
    if(tipo == "A"):
      tipo = 0
    elif (tipo == "B"):
      tipo = 1
    elif(tipo == "C"):
      tipo = 2
    elif(tipo == "D"):
      tipo = 3
    else:
      raise ValueError("\nTipo de Camisa inválido")

    return tipo

def tamanho(): # tamanho
    tamanho = input("Escolha o Tamanho(P/M/G): ").upper()
    if tamanho == "P":
      tamanho = 0
    elif(tamanho == "M"):
        tamanho = 1
    elif(tamanho == "G"):
        tamanho = 2
    else:
      raise ValueError("Tamanho invalido!")

    return tamanho

def adicionar(tip, tam):  # adicionar
  quantidade = int(input("\nQuantidade a Adicionar: "))

  if quantidade <= 0:
    raise ValueError("Quantidade inválida!")

  loja[tip][tam] += quantidade

  return loja[tip][tam]

def remover(tip, tam): # remover
  quantidade = (int(input("\nQuantidade a Remover: ")))

  disponivel = loja[tip][tam]

  if quantidade > disponivel:
    raise ValueError("Quantidade maior que o estoque!")

  if quantidade <= 0:
    raise ValueError("Quantidade inválida!")

  loja[tip][tam] -= quantidade

  return loja[tip][tam]

#interface
while True:
  print("\n===========  Gerencia. L O J A ============")
  print("[1] - Consultar um Modelo")
  print("[2] - Adicionar Estoque")
  print("[3] - RemoveR Estoque")
  print("[4] - Vizualizar Combinações com 3 ou menos")
  print("[0] - Sair")

  opc = int(input("Digite As Opções Acima: "))

  if (opc == 1): # verificar modelo

    tip = tipo()
    tam = tamanho()
    print(f'\nQuantidade Disponivel do Modelo: {loja[tip][tam]}')
    print()

  if(opc == 2): # adicionar

    tip = tipo()
    tam = tamanho()
    adc = adicionar(tip,tam)
    print(f'Novo Valor: {adc}')
    print()

    for i in range(len(loja)):
      print(loja[i])

  elif(opc == 3): # remover

    tip = tipo()
    tam = tamanho()
    rmv = remover(tip,tam)
    print(f'Novo Valor: {rmv}')
    print()

    for i in range(len(loja)):
      print(loja[i])

  elif(opc == 4): # exibe combinações com menos de 3

    for i in range(len(loja)): # 0 1 2 3
      print()
      for j in range(3) : # 012 012 012 012
        valor = loja[i][j]
        if (valor <= 3):

          if (j == 0):
            j = "P"
          elif (j == 1):
            j = "M"
          elif (j == 2):
            j = "G"

          if(i == 0):
            print(f"Camisa Tipo A, Tamanho {j}, Disponivel: {valor}")
          elif(i == 1):
            print(f"Camisa Tipo B, Tamanho {j}, Disponivel: {valor}")
          elif(i == 2):
            print(f"Camisa Tipo C, Tamanho {j}, Disponivel: {valor}")
          elif(i == 3):
            print(f"Camisa Tipo D, Tamanho {j}, Disponivel: {valor}")

  elif(opc == 0):
    print("\nVolte Sempre!")
    print("Estoque Final:")
    for i in range(len(loja)):
      print(loja[i])
    break

  else:
    print("\nInválido, Tente novamente!")
