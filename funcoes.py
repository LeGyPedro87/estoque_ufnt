
from salvamento import salvar_estoque,salvar_mod
mod = 0
def tamanho():
    while True:
        
        tamanho = input("Qual Tamanho(P/M/G):").upper()
        
        if(tamanho == "P"):
            return 0
        elif(tamanho == "M"):
            return 1
        elif(tamanho == "G"):
            return 2
        else:
            print("\n Tamanho Inválido!\n")

def modelos():
    while True:
        
        modelo = input("Digite o Modelo(1/2/3/4): ")
        
        if(modelo == "1"):
            return 0
        elif(modelo == "2"):
            return 1
        elif(modelo == "3"):
            return 2
        elif(modelo == "4"):
            return 3
        else:
            print("\nModelo Invalido!")


def adicionar(loja):
    global mod
    while True:
        
        tipo = modelos()
        tam = tamanho()
        adc = int(input("Quantidade a Adicionar: "))

        if (adc <= 0):
            print("\nValor invalido!\n")
            continue

        loja[tipo][tam] += adc  
        
        mod += 1 
        print("\nA operação foi concluida com Sucesso!")
        salvar_estoque(loja)
        salvar_mod(loja,"- Adição -",mod)
        break
        
def remover(loja):
  
    global mod
    while True:
        
        tipo = modelos()
        tam = tamanho()
        rmv = int(input("Quantidade a Remover: "))

        if (rmv <= 0):
            print("\nQuantidade inválida!\n")
            continue

        if (rmv > loja[tipo][tam]):
            print("\nQuantidade maior que estk!\n")
            continue

        loja[tipo][tam] -= rmv
        
        mod += 1
        print("\nA operação foi concluida com Sucesso!")
        salvar_estoque(loja)
        salvar_mod(loja,"- Remoção -", mod)
        break
