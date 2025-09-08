'''
Leia um arquivo que contenha dados de log de treinamento de modelos de Machine Learning. Calcule a média e o desvio padrão do tempo de exercução constantes.
'''

import pandas as pd


def processar_logs(nome_arquivo):
    try:
        df = pd.read_csv(nome_arquivo)
        media_tempo = df['tempo_execucao'].mean()
        desvio_padrao_tempo = df['tempo_execucao'].std()
        print(f'Média do tempo de execução: {media_tempo:.2f} segundos')
        print(f'Desvio padrão do tempo de execução: {desvio_padrao_tempo:.2f} segundos')
    except FileNotFoundError:
        print(f'Arquivo {nome_arquivo} não encontrado.')
    except Exception as e:
        print(f'Erro ao precessar o arquivo: {e}')

nome_arquivo = input('Digite o nome do arquivo de log: ')
processar_logs(nome_arquivo)
