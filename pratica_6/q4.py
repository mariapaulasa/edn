'''
Crie um programa que consulte a cotação atual de uma moeda estrangeira em relação ao Real Brasileiro (BRL). O usuário deve informar o código da moeda desejada (ex: USD, EUR, GBP), e o programa deve exibir o valor atual, máximo e mínimo da cotação, além da data e hora da última atualização. Utilize a API da AwesomeAPI para obter os dados de cotação.
'''
import requests

def consultar_cotacao(moeda):
    url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"
    try:
        resposta = requests.get(url)
        resposta.raise_for_status()  # Verifica se a requisição foi bem-sucedida
        dados = resposta.json()
        chave = f"{moeda}BRL"
        if chave not in dados:
            return "Moeda não encontrada. Verifique o código e tente novamente."
        
        cotacao = dados[chave]
        valor_atual = cotacao['bid']
        valor_maximo = cotacao['high']
        valor_minimo = cotacao['low']
        data_hora = cotacao['create_date']
        
        return (f"Cotação do {moeda} em relação ao BRL:\n"
                f"Valor Atual: R$ {valor_atual}\n"
                f"Valor Máximo: R$ {valor_maximo}\n"
                f"Valor Mínimo: R$ {valor_minimo}\n"
                f"Última Atualização: {data_hora}")
    except requests.exceptions.RequestException as e:
        return f"Erro ao acessar a API: {e}"
    except KeyError:
        return "Erro ao processar os dados da API."
    
def main():
    moeda = input("Digite o código da moeda (ex: USD, EUR, GBP): ").upper()
    print('Consultando a cotação...')
    resultado = consultar_cotacao(moeda)
    print(resultado)        

if __name__ == "__main__":
    main()  