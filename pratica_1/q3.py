# Calculador de volume

'''
Crie um programa que calcule o volume de uma caixa retangular. Use as seguintes dimensões:
Comprimento: 12 cm
Largura: 14 cm
Altura: 20 cm 
O programa deve calcular o volume e exibir o resultado em cm³.
'''
comprimento = int(input("Digite o comprimento da caixa em cm: "))
largura = int(input("Digite a largura da caixa em cm: "))       
altura = int(input("Digite a altura da caixa em cm: "))

volume = comprimento * largura * altura 

print(f"O volume da caixa com as medidas {comprimento}x{largura}x{altura}cm é de {volume} cm³")
