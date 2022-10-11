class Tabela:
    tabela = None

    def __init__(self):
        self.tabela = [ ]

    def insere_linhas(self,quantidadeLinhas):
        for i in range(quantidadeLinhas):
            self.tabela.append([])
        print("Quantidade de Linhas adicionadas " + str(quantidadeLinhas) + "\n")

    def insere_colunas(self,quantidadeColunas):
        for i in range(len(self.tabela)):
            for j in range(quantidadeColunas):
                self.tabela[i].append([])

        print("Quantidade de Colunas adicionadas " + str(quantidadeColunas) + "\n")

    def valor(self,linha,coluna):
        print("O valor que esta contido na Linha: " + str(linha) + " Coluna: " + str(coluna))
        return str(self.tabela[linha][coluna])


    def altera_valor(self,linha,coluna,valor):
        if((len(self.tabela) - 1 )>= linha and (len(self.tabela[0]) - 1) >= coluna):
            self.tabela[linha][coluna] = valor
            print("O valor da linha "+ str(linha) + " coluna"+ str(coluna) + " Foi alterado para: "+
                 str(valor) +"\n")
        else:
            print("A coluna e a linha nao existe")

    def __repr__(self):
        texto  = ""

        for i in range(len(self.tabela)):
            texto+= str(self.tabela[i]) + "\n"

        return texto

objeto = Tabela()
objeto.insere_linhas(3)
print(objeto)
objeto.insere_colunas(4)
print(objeto)
objeto.altera_valor(2,1,40)
print(objeto)
objeto.altera_valor(2,2,50)
print(objeto)
print(objeto.valor(2,2))