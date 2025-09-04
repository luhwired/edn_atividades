#!/usr/bin/python3
#-*-coding:utf-8-*-

import random
import string

def gerar_senha(tamanho):
    if tamanho < 4:
        print("Erro: O tamanho da senha deve ser de no minimo 4 caracteres para garantir a seguranca.")
        return None

    letras_maiusculas = string.ascii_uppercase
    letras_minusculas = string.ascii_lowercase
    numeros = string.digits
    simbolos = string.punctuation
    senha_garantida = [
        random.choice(letras_maiusculas),
        random.choice(letras_minusculas),
        random.choice(numeros),
        random.choice(simbolos),
    ]

    pool_completo = letras_maiusculas + letras_minusculas + numeros + simbolos
    senha_restante = [random.choice(pool_completo) for _ in range(tamanho - 4)]

    lista_senha = senha_garantida + senha_restante
    random.shuffle(lista_senha)

    return "".join(lista_senha)

try:
    comprimento = int(input("Digite a quantidade de caracteres para a senha: "))
    senha_gerada = gerar_senha(comprimento)
    
    if senha_gerada:
        print(f"\nSua senha aleatoria é: {senha_gerada}")

except ValueError:
    print("Erro: Por favor, digite um numero valido.")