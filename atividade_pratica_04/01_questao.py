#!/usr/bin/python3
# -*- coding: utf-8 -*-

def calcular(a: float, b: float, operador: str) -> float:
    """Executa operações matemáticas básicas."""
    if operador == "+":
        return a + b
    elif operador == "-":
        return a - b
    elif operador == "*":
        return a * b
    elif operador == "/":
        if b == 0:
            raise ZeroDivisionError("Divisão por zero não permitida.")
        return a / b
    else:
        raise ValueError("Operador inválido! Use +, -, * ou /.")

def main():
    try:
        a = float(input("Digite o primeiro número: "))
        b = float(input("Digite o segundo número: "))
        operador = input("Digite a operação (+, -, *, /): ")

        resultado = calcular(a, b, operador)
        print(f"Resultado: {a} {operador} {b} = {resultado}")
    except Exception as e:
        print(f"Erro: {e}")

    print("Fim do programa.")

if __name__ == "__main__":
    main()

