'''
Crie um script em Python que escreva dados em um arquivo CSV. O arquivo CSV deve conter informações pessoais, como colunas Nome, Idade e Cidade.
'''

import csv

def escrever_csv(nome_arquivo, dados):
    try:
        with open(nome_arquivo, mode='w', newline='') as arquivo:
            escritor = csv.writer(arquivo)
            escritor.writerow(['Nome', 'Idade', 'Cidade'])
            for linha in dados:
                escritor.writerow(linha)
        print(f'Dados escritos no arquivo {nome_arquivo} com sucesso.')
    except Exception as e:  
        print(f'Erro ao escrever no arquivo: {e}')  

def main():

    dados = [ 
        ['Ana', 28, 'São Paulo'],
        ['Bruno', 34, 'Rio de Janeiro'],    
        ['Carla', 22, 'Belo Horizonte'] 
    ]


    nome_arquivo = input('Digite o nome do arquivo CSV para salvar os dados: ').strip()
    escrever_csv(nome_arquivo, dados)

if __name__ == '__main__':
    main()