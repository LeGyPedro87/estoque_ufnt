

def salvar_estoque(loja):
    with open("estoque.txt", "w", encoding="utf-8") as arquivo:
        for linha in range(4):
            for coluna in range(3):
                arquivo.write(f"{loja[linha][coluna]}")

                if coluna < 2:
                    arquivo.write(";")

            arquivo.write("\n")

    return ("\nSalvo Com Sucesso!\n")

def Salvar_mod(loja,msg,mod):
    with open("modify.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(f"\nModificação: {mod} - {msg} -\n")
        for linha in range(4):
            for coluna in range(3):
                arquivo.write(f"{loja[linha][coluna]}")

                if coluna < 2:
                    arquivo.write(";")

            arquivo.write("\n")
    return ("\n Modificação Salva!\n")
