'''
Desenvolva um programa que consulte informações de endereço a partir de um CEP fornecido pelo usuário, utilizando a API ViaCEP. O programa deve exibir o logradouro, bairro, cidade e estado correspondentes ao CEP consultado.'''

import requests
import json

def consultar_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"   
    resposta = requests.get(url)        

    try:
        resposta = requests.get(url)
        resposta.raise_for_status()  # Verifica se a requisição foi bem-sucedida
        dados = resposta.json()
        if 'erro' in dados:
            return "CEP não encontrado."
        logradouro = dados.get('logradouro', 'N/A')
        bairro = dados.get('bairro', 'N/A')
        cidade = dados.get('localidade', 'N/A')
        estado = dados.get('uf', 'N/A')
        return f'\nLogradouro: {logradouro}, \nBairro: {bairro}, \nCidade: {cidade}, \nEstado: {estado}'
    except requests.exceptions.RequestException as e:
        return f"Erro ao acessar a API: {e}"  
          
    
def main():
    cep = input("Digite o CEP (somente números): ")
    if not cep.isdigit() or len(cep) != 8:
        print("CEP inválido. Certifique-se de que contém 8 dígitos numéricos.")
        return

    print('Consultando o CEP...')
    resultado = consultar_cep(cep)
    print(resultado)
    
if __name__ == "__main__":
    main() 