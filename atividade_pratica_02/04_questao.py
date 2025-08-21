#!/usr/bin/python3
#-*-coding:utf-8-*-

distancia_percorrida = 300
combustivel_gasto = 25

consumo_medio = distancia_percorrida / combustivel_gasto

print('--- Dados da Viagem ---')
print(f'Distância percorrida: {distancia_percorrida} km')
print(f'Combustível gasto: {combustivel_gasto} litros')
print(f'-----------------------')
print(f'Consumo médio: {consumo_medio:.2f} km/l')
print('-----------------------')
