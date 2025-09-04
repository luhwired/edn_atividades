#!/usr/bin/python3
#-*-coding:utf-8-*-

def calcular_desconto(preco_original, percentual_desconto):
    valor_desconto = preco_original * (percentual_desconto / 100)
    preco_final = preco_original - valor_desconto
    valor_desconto_arredondado = round(valor_desconto, 2)
    preco_final_arredondado = round(preco_final, 2)

    return valor_desconto_arredondado, preco_final_arredondado

print("--- Calculadora de Descontos ---")

try:
    preco = float(input("Digite o preço original do produto: R$ "))
    percentual = float(input("Digite a porcentagem de desconto (apenas o número): % "))
    
    if preco < 0 or percentual < 0:
        print("\nErro: Por favor, insira valores positivos para preço e desconto.")
    else:
        desconto, preco_com_desconto = calcular_desconto(preco, percentual)

        print("\n---------------------------------")
        print(f"Preço original: R$ {preco:.2f}")
        print(f"Percentual de desconto: {percentual}%")
        print(f"Valor do desconto: R$ {desconto:.2f}")
        print(f"Preço final com desconto: R$ {preco_com_desconto:.2f}")
        print("---------------------------------")

except ValueError:
    print("\nErro: Valor inválido. Por favor, digite apenas números.")