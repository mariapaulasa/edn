'''
Crie uma função que calcule a idade de uma pessoa em dias, baseada no ano de nascimento.mv
'''

def calcular_idade_em_dias(ano_nascimento, ano_atual):
    idade_anos = ano_atual - ano_nascimento
    idade_dias = idade_anos * 365  # Ignorando anos bissextos para simplificação
    return idade_dias   

def main():
    ano_nascimento = 1990
    ano_atual = 2024
    
    idade_dias = calcular_idade_em_dias(ano_nascimento, ano_atual)
    
    print(f"A pessoa tem {idade_dias} dias de idade.")  


if __name__ == "__main__":
    main()  