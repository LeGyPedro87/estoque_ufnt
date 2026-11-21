
loja = [

    [3,5,7],
    [6,7,9],
    [9,5,4],
    [1,6,7]

]

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