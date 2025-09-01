'''
Crie uma função que calcule a gorjeta a ser deixada em um restaurante, baseada no valor total da conta e na porcentagem de gorjeta desejada. Calcula o valor da gorjeta baseado no total da conta e na porcentagem desejada.
Parâmetros: valor_conta (float): O valor total da conta porcentagem_gorjeta (float): A porcentagem da gorjeta (ex: 15 para 15%)
Retorna: float: O valor da gorjeta calculada

'''

def calcular_gorjeta(valor_conta, porcentagem_gorjeta):
    gorjeta = round(valor_conta * (porcentagem_gorjeta / 100), 2)
    return gorjeta

def main():
    valor_conta = 150.00
    porcentagem_gorjeta = 15
    
    gorjeta = calcular_gorjeta(valor_conta, porcentagem_gorjeta)
    
    print(f"Valor da Conta: R$ {valor_conta}")
    print(f"Porcentagem de Gorjeta: {porcentagem_gorjeta}%")
    print(f"Valor da Gorjeta: R$ {gorjeta}")

if __name__ == "__main__":
    main()

    