#!/usr/bin/python3
#-*-coding:utf-8-*-

from datetime import date

def calcular_dias_vividos(ano_nascimento, mes_nascimento, dia_nascimento):
    try:
        data_nascimento = date(ano_nascimento, mes_nascimento, dia_nascimento)
        
        data_hoje = date.today()
        
        if data_nascimento > data_hoje:
            print("Erro: A data de nascimento não pode ser no futuro.")
            return None
        diferenca = data_hoje - data_nascimento
        return diferenca.days
    except ValueError:
        print("Erro: A data que você inseriu é inválida.")
        return None

print("--- Calculadora de Dias Vividos ---")

try:
    ano = int(input("Digite o seu ano de nascimento (ex: 1995): "))
    mes = int(input("Digite o seu mês de nascimento (ex: 7): "))
    dia = int(input("Digite o seu dia de nascimento (ex: 21): "))
    total_dias = calcular_dias_vividos(ano, mes, dia)

    if total_dias is not None:
        print("\n-------------------------------------------")
        print(f"Até hoje, você viveu {total_dias:,d} dias.".replace(',', '.'))
        print("-------------------------------------------")

except ValueError:
    print("Erro: Por favor, digite apenas números para a data.")