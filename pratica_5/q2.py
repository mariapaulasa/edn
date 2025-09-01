'''
Crie uma função que verifique se uma palavra ou frase é um palíndromo (lê-se igual de trás para frente, ignorando espaços e pontuação). Se o resultado é True, responda “Sim”, se o resultado for False, responda “Não”.

'''

import re       

def eh_palindromo(texto):
    texto_limpo = re.sub(r'[^A-Za-z0-9]', '', texto).lower()
    return texto_limpo == texto_limpo[::-1]


def main():     
    texto = "Socorram-me, subi no ônibus em Marrocos"   
    resultado = eh_palindromo(texto)    
    resposta = "Sim" if resultado else "Não"
    print(f"O texto é um palíndromo? {resposta}")

if __name__ == "__main__":
    main()
     



