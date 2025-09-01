'''
Crie um programa que gera um perfil de usuário aleatório usando a API 'Random User Generator'. O programa deve exibir o nome, email e país do usuário gerado.
'''


import requests
import json

def obter_usuario_aleatorio():
    url = "https://randomuser.me/api/"
    resposta = requests.get(url)
    
    try:
        responce = requests.get(url)
        responce.raise_for_status()  # Verifica se a requisição foi bem-sucedida
        dados = responce.json()['results'][0]
        nome = f'{dados['name']['first']} {dados['name']['last']}'
        email = dados['email']
        pais = dados['location']['country']
        return f'Nome: {nome}, email: {email}, país: {pais}'
    except requests.exceptions.RequestException as e:
        print(f"Erro ao acessar a API: {e}")
        return None

def main():

    print('Gerando um usuário aleatório...')
    usuario = obter_usuario_aleatorio()
    print(usuario)
    
if __name__ == "__main__":
    main()       
