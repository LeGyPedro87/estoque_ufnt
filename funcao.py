
def tamanho():
    while True:
        tamanho = input("Qual Tamanho(P/M/G):").upper()

        if tamanho == "P":
            return 0
        elif tamanho == "M":
            return 1
        elif tamanho == "G":
            return 2
        else:
            print("\n Tamanho Inválido!\n")

''''
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
'''