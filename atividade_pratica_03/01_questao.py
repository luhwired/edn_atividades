#!/usr/bin/python3
# -*- coding: utf-8 -*-

def classificar_idade(idade: int) -> str:
    if idade < 0:
        return "Idade inválida!"
    elif idade <= 12:
        return "Você é uma criança."
    elif idade <= 17:
        return "Você é um adolescente."
    elif idade <= 59:
        return "Você é um adulto."
    else:
        return "Você é um idoso."

def main():
    try:
        idade = int(input("Digite a sua idade: "))
        print(classificar_idade(idade))
    except ValueError:
        print("Entrada inválida! Digite apenas números.")
    print("Fim do programa.")

if __name__ == "__main__":
    main()
