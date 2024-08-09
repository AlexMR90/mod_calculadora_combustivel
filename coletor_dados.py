class Coletor:
    def __init__(self):
        self.valor_alcool: float
        self.valor_diesel: float
        self.valor_gasolina: float
        self.distancia: float
        self.combustivel: float
        self.opcao: int
    

    def coletar_distancia(self):
        self.distancia = float(input("Qual a distância a ser percorrida? "))
        return self.distancia
    
    def coletar_combustivel(self):
        self.combustivel = float(input("Qual o consumo de combustível (km/l) do carro? "))
        return self.combustivel
    
    def coletar_valor_alcool(self):
        self.valor_alcool = float(input("Qual o valor atual do Álcool? "))
        return self.valor_alcool

    def coletar_valor_diesel(self):
        self.valor_diesel= float(input("Qual o valor atual do diesel? "))
        return self.valor_diesel
    
    def coletar_valor_gasolina(self):
        self.valor_gasolina = float(input("Qual o valor atual da gasolina? "))
        return self.valor_gasolina
    
    def coletar_opcao(self):
        self.opcao = int(input("Digite a opção desejada: "))
        if self.opcao == 1:
            
            self.coletar_valor_alcool()
        elif self.opcao == 2:
            
            self.coletar_valor_diesel()

        elif self.opcao == 3:
            
            self.coletar_valor_gasolina()
        elif self.opcao == 4:
            self.coletar_valor_alcool()
            self.coletar_valor_diesel()
            self.coletar_valor_gasolina()
        else:
            print("opção inválida")
            exit()
        return self.opcao



        