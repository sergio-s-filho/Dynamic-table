class Tabela:
    tabela = None
    quantidadeColunas = 0

    def __init__(self):
        self.tabela = [ ]

    def insere_linhas(self,quantidadeLinhas):
        for i in range(quantidadeLinhas):
            self.tabela.append([])
            for j in range(len(self.tabela[0])):
               self.tabela[len(self.tabela) - 1].append([])

        print("Quantidade de Linhas adicionadas " + str(quantidadeLinhas) + "\n")

    def insere_colunas(self,quantidadeColunas):
        for i in range(len(self.tabela)):
            for j in range(quantidadeColunas):
                self.tabela[i].append([])

        print("Quantidade de Colunas adicionadas " + str(quantidadeColunas) + "\n")


    def __repr__(self):
        texto  = ""

        for i in range(len(self.tabela)):
            texto+= str(self.tabela[i]) + "\n"

        return texto

objeto = Tabela()
objeto.insere_linhas(1)
print(objeto)
objeto.insere_linhas(3)
print(objeto)
objeto.insere_colunas(4)
print(objeto)
objeto.insere_linhas(3)
print(objeto)
objeto.insere_linhas(4)
print(objeto)
objeto.insere_colunas(7)
print(objeto)
