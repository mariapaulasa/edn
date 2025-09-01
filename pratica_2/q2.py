'''
2- Calculadora de Desconto 

Desenvolva um programa que calcula o desconto em uma loja. Use as seguintes informações:

Nome do produto: "Camiseta"

Preço original: R$ 50.00

Porcentagem de desconto: 20% 
O programa deve calcular o valor do desconto e o preço final, exibindo todos os detalhes.
'''

def calcular_desconto(preco_original, porcentagem_desconto):
    valor_desconto = round(preco_original * (porcentagem_desconto / 100), 2)
    preco_final = round(preco_original - valor_desconto, 2)
    return valor_desconto, preco_final  

def main():
    nome_produto = "Camiseta"
    preco_original = 50.00
    porcentagem_desconto = 20
    
    valor_desconto, preco_final = calcular_desconto(preco_original, porcentagem_desconto)
    
    print(f"Produto: {nome_produto}")
    print(f"Preço Original: R$ {preco_original}")
    print(f"Porcentagem de Desconto: {porcentagem_desconto}%")
    print(f"Valor do Desconto: R$ {valor_desconto}")
    print(f"Preço Final: R$ {preco_final}")

if __name__ == "__main__":
    main()  