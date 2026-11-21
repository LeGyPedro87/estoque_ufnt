
from salvamento import salvar_estoque,Salvar_mod

#from funcao import tamanho


tamanhos = ["P","M","G"]
models = ["Modelo 1", "Modelo 2", "Modelo 3", "Modelo 4"]
mod =0

try:
    with open("estoque.txt", "r", encoding="utf-8") as arquivo:
        linhas = arquivo.readlines()

        loja = []
        for linha in linhas[0:5]:
            numeros = linha.strip().split(";")
            loja.append([int(numero) for numero in numeros])

except FileNotFoundError:
    print("\nArquivo não encontrado. Iniciando estoque padrão.\n")

    loja = []

    for i in range(4): # Roda o Modelo
        modelo = []
        for x in range(3): # Roda o Tamanho
            quant = int(input(f"Quantidade do Modelo {i+1},Tamanho {tamanhos[x]}: "))
            modelo.append(quant)
        loja.append(modelo)

    salvar_estoque(loja)
  
  
    
    
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
            
            
            
            
            
while True:

    print("\n======= LoJa JoJa ========\n") #Exibe Estoque Ao voltar para o While
    print("LoJa      P  M  G")
    for i in range(4):
        print(models[i], end =" ")
        print(loja[i])

    print("\n[1] - Adicionar\n[2] - Remover\n[3] - Ver Menores que 3\n[0] - Sair")
    opc = int(input("Digite a Opção: "))

    if(opc == 1):# Adicionar

        tipo = int(input("\nTipo de camisa: "))
        tam1 = tamanho()
        adc = int(input("Quantidade a Adicionar: "))
        
        if adc <= 0:
            print("\nValor invalido!\n")
            continue

        loja[tipo -1][tam1] += adc

        mod += 1
        salvar_estoque(loja)
        Salvar_mod(loja,"ADIÇÃO",mod)

    if(opc == 2): # Remoção

        tipo = int(input("\nTipo de camisa: "))
        tam2 = tamanho()
        rmv = int(input("Quantidade a Remover: "))

        if rmv <= 0:
            print("\nQuantidade inválida!\n")
            continue

        if rmv > loja[tipo -1][tam2]:
            print("\nQuantidade maior que estk!\n")
            continue

        loja[tipo -1][tam2] -= rmv
        mod += 1
        salvar_estoque(loja)
        Salvar_mod(loja,"REMOÇÃO",mod)

    if(opc == 3): # Contar < 3
         for i in range(len(loja)): # 0 1 2 3
              print()
              for j in range(3) : # 012 012 012 012
                valor = loja[i][j]

                if loja[i][j] <= 3:
                    print(f"Camisa Modelo {i+1}, Tamanho {tamanhos[j]}, Disponivel: {valor}")

    if(opc == 0):
        print("\nVolte Sempre!")
        break

print()
for i in range(len(loja)):
  print(loja[i])

