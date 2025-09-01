'''
1- Conversor de Moeda 

Crie um programa que converte um valor em reais para dólares e euros. Use os seguintes dados:

Valor em reais: R$ 100.00

Taxa do dólar: R$ 5.60

Taxa do euro: R$ 6.60 
O programa deve calcular e exibir os valores convertidos, arredondando para duas casas decimais.
'''

def converter_moeda(valor_reais, taxa_dolar, taxa_euro):
    valor_dolar = round(valor_reais / taxa_dolar, 2)
    valor_euro = round(valor_reais / taxa_euro, 2)
    return valor_dolar, valor_euro      

def main():
    valor_reais = 100.00
    taxa_dolar = 5.60
    taxa_euro = 6.60
    
    valor_dolar, valor_euro = converter_moeda(valor_reais, taxa_dolar, taxa_euro)
    
    print(f"Valor em Reais: R$ {valor_reais}")
    print(f"Valor em Dólares: $ {valor_dolar}")
    print(f"Valor em Euros: € {valor_euro}")

if __name__ == "__main__":
    main()