import random


class Tabela:
    tabela = None

    def __init__(self):
        self.tabela = []


    # -----------------------------------------------------------------------
    
    # @param quantidadeLinhas: quantidade de linhas no qual queremos inserir em nossa tabela
    # adiciona linhas na tabela, cada linha adicionada na tebela, deve respeitar a quantidade de
    # colunas ja inseridas em outras linhas


    def insereLinhas(self, quantidadeLinhas):
        for i in range(quantidadeLinhas):
            self.tabela.append([])
            for j in range(len(self.tabela[0])):
                self.tabela[len(self.tabela) - 1].append([])

        print("Quantidade de Linhas adicionadas " + str(quantidadeLinhas) + "\n")


    # #------------------------------------------------------------------------------------
    # @param quantidadeColunas: quantidade de colunas no qual queremos inserir em nossa tabela
    # adiciona colunas em nossa tabela, a quantidade de linhas adicionadas deve ser adicionada
    # em todas as linhas,para manter a tabela de forma dinamica

    def insereColunas(self, quantidadeColunas):
        for i in range(len(self.tabela)):
            for j in range(quantidadeColunas):
                self.tabela[i].append([])

        print("Quantidade de Colunas adicionadas " + str(quantidadeColunas) + "\n")
    #------------------------------------------------------------------------------------
    
    # @param linha: linha no qual queremos remover
    # remove a linha e todas as suas colunas

    def removerLinha(self,linha: int):
        print("Linha removida " + str(linha))
        self.tabela.pop(linha)


    #------------------------------------------------------------------------------------
    
    # @param coluna valor referente a coluna a ser removida
    # remove a coluna passada como parametro de todas as linhas da tabela

    def removeColuna(self,coluna: chr):
        print("Coluna removida " + str(coluna))
        aux = ord(coluna) - 65
        for i in range(len(self.tabela)):
            self.tabela[i].pop(aux)

    #------------------------------------------------------------------------------------
    
    # @param linha: linha no qual queremos alterar o valor
    # @param coluna: coluna( no formato de character A -- Z ) no qual queremos alterar o valor
    # @param valor:  valor no qual queremos alterar em nossa tabela
    # passado a linha e a coluna e o valor para ser alterado, faz a alteração do mesmo para o novo valor


    def alteraValor(self, linha: int, coluna: chr, valor):
        tempValue = self.tabela[linha][ord(coluna) - 65]
        self.tabela[linha][ord(coluna) - 65] = valor

        print("o valor: " + str(tempValue) + " que estava na Linha: " + str(linha + 1) + " e coluna: " + str(coluna) + " foi alterado para o valor " + str(valor) + "\n")


    #------------------------------------------------------------------------------------

    # @param linha: linha no qual queremos buscar o valor
    # @pram coluna: coluna no qual queremos buscar o valor
    # mostra o valor que esta contido na linha X e coluna Y

    def mostrarValor(self, linha:int ,coluna:chr ):
        print("o valor: que esta contido na Linha: " + str(linha + 1) + " e na Coluna: " + coluna + " é: " + str(self.tabela[linha][ord(coluna) - 65]) + "\n")


    #------------------------------------------------------------------------------------
    
    # constroi a representação visual da nossa tabela, nossas linhas sao numeradas de 1 -> n, onde n é o quantidade
    # de linha de nossa tabela, as colunas sao indexadas de A - Z , onde utilizei o valor decimal de cada Char da
    # tabela ASCII para indexar cada coluna de acordo com a ordem do alfabeto

    def __repr__(self):
        texto = ""
        for i in range(len(self.tabela[0])):
            texto += "   " + chr(65 + i)
        for i in range(len(self.tabela)):
            texto += "\n" + str(i + 1) + " " + str(self.tabela[i])
        return texto + "\n"


