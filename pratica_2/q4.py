'''
4- Calculadora de Consumo de Combustível

 Desenvolva um programa que calcula o consumo médio de combustível de um veículo. Use os seguintes dados:

Distância percorrida: 300 km

Combustível gasto: 25 litros 
O programa deve calcular o consumo médio (km/l) e exibir todos os dados da viagem, incluindo o resultado final arredondado para duas casas decimais.

'''

def calcular_consumo(distancia_km, combustivel_litros):
    consumo_medio = round(distancia_km / combustivel_litros, 2)
    return consumo_medio    

def main():     
    distancia_km = 300
    combustivel_litros = 25
    
    consumo_medio = calcular_consumo(distancia_km, combustivel_litros)
    
    print(f"Distância Percorrida: {distancia_km} km")
    print(f"Combustível Gasto: {combustivel_litros} litros")
    print(f"Consumo Médio: {consumo_medio} km/l")

if __name__ == "__main__":
    main()