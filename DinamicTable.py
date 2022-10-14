class Tabela:
    tabela = None

    def __init__(self):
        self.tabela = []
        
    #adiciona linhas na tabela, cada linha adicionada na tebela, deve respeitar a quantidade de colunas ja inseridas em outras linhas
    def insereLinhas(self,quantidadeLinhas):
        for i in range(quantidadeLinhas):
            self.tabela.append([])
            for j in range(len(self.tabela[0])):
               self.tabela[len(self.tabela) - 1].append([])

        print("Quantidade de Linhas adicionadas " + str(quantidadeLinhas) + "\n")

    #adiciona colunas em nossa tabela, a quantidade de linhas adicionadas deve ser adicionada em todas as linhas , para manter a matriz de forma dinamica
    def insereColunas(self,quantidadeColunas):
        for i in range(len(self.tabela)):
            for j in range(quantidadeColunas):
                self.tabela[i].append([])

        print("Quantidade de Colunas adicionadas " + str(quantidadeColunas) + "\n")

    #passado a linha e a coluna e o valor para ser alterado, faz a alteração do mesmo para o novo valor
    def alteraValor(self,linha,coluna,valor):
        tempValue = self.tabela[linha][coluna]
        self.tabela[linha][coluna] = valor

        print("o valor: " + str(tempValue) + " que estava na Linha: " + str(linha + 1) + " e coluna: " + chr(65 + (coluna)) + " foi alterado para o valor " + str(valor) + "\n")

    #mostra o valor que esta contido na linha X e coluna Y
    def mostrarValor(self,linha,coluna):
        print("o valor: que esta contido na Linha: " + str(linha + 1) + " e na Coluna: " + chr(65 + (coluna)) + " é: " + str(self.tabela[linha][coluna]) + "\n")
    
    #representação visual do nosso Objeto
    def __repr__(self):
        texto  = ""

        for i in range(len(self.tabela[0])):
            texto+= "   " + chr(65 + i)

        for i in range(len(self.tabela)):
            texto+= "\n" + str(i + 1) + " "+ str(self.tabela[i])

        return texto + "\n"

objeto = Tabela()
objeto.insereLinhas(1)
print(objeto)
objeto.insereLinhas(3)
print(objeto)
objeto.insereColunas(4)
print(objeto)
objeto.insereLinhas(3)
print(objeto)
objeto.insereLinhas(2)
print(objeto)
objeto.insereColunas(7)
print(objeto)
objeto.alteraValor(5,5,20)
print(objeto)
objeto.retornaValor(5,5)
print(objeto)



