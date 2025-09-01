'''
Crie um programa que gera uma senha aleatória com o módulo random, utilizando caracteres especiais, possibilitando o usuário a informar a quantidade de caracteres dessa senha aleatória.

'''

import random 
import string

def gerar_senha(tamanho):

    #if tamanho < 4:
    #    print("O tamanho da senha deve ser pelo menos 4 para incluir todos os tipos #de caracteres.")
    #    return None

    caracteres = string.ascii_letters + string.digits + "!@#$%&*"
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

tamanho_senha = int(input("Digite o tamanho desejado para a senha: "))
senha_gerada = gerar_senha(tamanho_senha)

print(f"Senha gerada: {senha_gerada}")