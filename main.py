
from salvamento import salvar_estoque,salvar_mod
from funcoes import tamanho, modelos, adicionar, remover


tamanhos = ["P","M","G"]
models = ["Modelo 1", "Modelo 2", "Modelo 3", "Modelo 4"]
mod = 0

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
                 
while True:

    print("\n======= LoJa JoJa ========\n") #Exibe Estoque Ao voltar para o While
    print("LoJa      P  M  G")
    
    for i in range(4):
        print(models[i], end =" ")
        print(loja[i])

    print("\n[1] - Adicionar\n[2] - Remover\n[3] - Ver Menores que 3\n[0] - Sair")
    opc = int(input("Digite a Opção: "))

    if(opc == 1):# Adicionar
      pass
        
    elif(opc == 2): # Remoção
      pass

    if(opc == 3):
      
         for i in range(len(loja)): # 0 1 2 3
              print()
              for j in range(3) : # 012 012 012 012
                valor = loja[i][j]

                if loja[i][j] <= 3:
                    print(f"Camisa Modelo {i+1}, Tamanho {tamanhos[j]}, Disponivel: {valor}")

    if(opc == 0):
      print("\nVolte Sempre!")
      break
