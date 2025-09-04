#!/usr/bin/python3
#-*-coding:utf-8-*-

def calcular_gorjeta_completo(valor_conta, porcentagem_gorjeta=10.0):
    valor_gorjeta = round(valor_conta * (porcentagem_gorjeta / 100), 2)
    valor_final = valor_conta + valor_gorjeta
    return valor_gorjeta, valor_final

try:
    total_conta = float(input("Digite o valor total da conta: "))
    input_porcentagem = input("Digite a porcentagem da gorjeta (padrão é 10%): ")

    if input_porcentagem:
        porcentagem = float(input_porcentagem)
        gorjeta, total_final = calcular_gorjeta_completo(total_conta, porcentagem)
    else:
        gorjeta, total_final = calcular_gorjeta_completo(total_conta)
    print(f"\nO valor da gorjeta é: R$ {gorjeta:.2f}")
    print(f"O valor total a ser pago é: R$ {total_final:.2f}")

except ValueError:
    print("Erro: Por favor, digite um valor numérico válido.")