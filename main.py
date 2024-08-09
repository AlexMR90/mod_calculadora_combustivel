from calculadora import Calculo
from coletor_dados import Coletor

def main():
    print(
        """
Esta aplicação tem como finalidade demonstrar os valores que serão gastos
com combustível durante uma viagem, com base no consumo do seu veículo, e
com a distância determinada por você sendo as opções de combustíveis: álcool, diesel e gasolina
        """
    )

    print("""
Escolha pelo número a opção desejada:\n 
1 - Álcool
2 - Diesel
3 - Gasolina
4 - Comparar com todos os combustíveis
        """
        )
    coletor = Coletor()
    coletor.coletar_opcao()
    coletor.coletar_combustivel()
    coletor.coletar_distancia()
    calculo = Calculo(coletor)
    print(
                "\nSegue o custo da sua viagem: ",
        calculo.calculo_custo())
    


if __name__=="__main__":
    main()    