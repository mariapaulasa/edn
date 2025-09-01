'''

Crie um programa que receba o preço original de um produto e um percentual de desconto, realizando o cálculo do preço final após a aplicação do desconto. Requisitos:
Permitir que o usuário informe o preço do produto e o percentual de desconto.
Utilizar operações matemáticas para calcular o valor do desconto e o preço final.
Exibir o preço final com duas casas decimais para garantir precisão. Entrada esperada: preço do produto (exemplo: 250.75) e o percentual de desconto (exemplo: 10).

'''

def calcular_preco_final(preco_original, percentual_desconto):
    valor_desconto = round(preco_original * (percentual_desconto / 100), 2)
    preco_final = round(preco_original - valor_desconto, 2)
    return preco_final  

def main():
    preco_original = float(input("Informe o preço do produto: R$ "))
    percentual_desconto = float(input("Informe o percentual de desconto: "))
    
    preco_final = calcular_preco_final(preco_original, percentual_desconto)
    
    print(f"Preço Original: R$ {preco_original:.2f}")
    print(f"Percentual de Desconto: {percentual_desconto}%")
    print(f"Preço Final após Desconto: R$ {preco_final:.2f}")

if __name__ == "__main__":
    main()
    