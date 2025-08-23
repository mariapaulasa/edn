# Calculadora de Preço Total

'''
Desenvolva um programa que calcule o preço total de uma compra. 
Use as seguintes informações:

Nome do produto: "Cadeira Infantil"
Preço unitário: R$ 12.40
Quantidade: 3 
O programa deve calcular o preço total e exibir todas as informações, 
incluindo o resultado final.
'''


produto = "Cadeira Infantil"
preco_uni = 12.40
print(f"Produto: {produto} - Preço Unitário: R$ {preco_uni:.2f}")
qtde = int(input("Digite a quantidade de cadeiras que deseja comprar: "))
preco_total = preco_uni * qtde

print(f"O preço unitário do produto é: R$ {preco_uni:.2f} x {qtde} unidades = R$ {preco_total:.2f}")
