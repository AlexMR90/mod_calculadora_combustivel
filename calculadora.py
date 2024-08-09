from coletor_dados import Coletor    
class Calculo:
    
    def __init__(self,coletor:Coletor):
        self.coletor = coletor
        


    def calculo_custo(self):
        if self.coletor.opcao == 1:
            return (self.coletor.distancia / self.coletor.combustivel )* self.coletor.valor_alcool
            
        elif self.coletor.opcao == 2:
            return (self.coletor.distancia / self.coletor.combustivel )* self.coletor.valor_diesel
            
        elif self.coletor.opcao == 3:
            return  (self.coletor.distancia / self.coletor.combustivel )* self.coletor.valor_gasolina
        elif self.coletor.opcao == 4:
            custo_alcool = (self.coletor.distancia / self.coletor.combustivel )* self.coletor.valor_alcool
            custo_diesel = (self.coletor.distancia / self.coletor.combustivel )* self.coletor.valor_diesel
            custo_gasolina = (self.coletor.distancia / self.coletor.combustivel )* self.coletor.valor_gasolina
            return """
                    
                Álcool: {}
                Diesel: {}
                Gasolina: {}
                   """.format(custo_alcool,custo_diesel,custo_gasolina)
            
        


        