#!/usr/bin/python3
# -*- coding: utf-8 -*-

def converter_temperatura(valor: float, origem: str, destino: str) -> float:
    """Converte temperatura entre Celsius, Fahrenheit e Kelvin."""
    origem = origem.upper()
    destino = destino.upper()

    if origem == destino:
        return valor

    if origem == "C":
        celsius = valor
    elif origem == "F":
        celsius = (valor - 32) * 5/9
    elif origem == "K":
        celsius = valor - 273.15
    else:
        raise ValueError("Unidade de origem inválida. Use C, F ou K.")

    if destino == "C":
        return celsius
    elif destino == "F":
        return (celsius * 9/5) + 32
    elif destino == "K":
        return celsius + 273.15
    else:
        raise ValueError("Unidade de destino inválida. Use C, F ou K.")


def main():
    try:
        temperatura = float(input("Digite a temperatura: "))
        origem = input("Digite a unidade de origem (C, F ou K): ")
        destino = input("Digite a unidade de destino (C, F ou K): ")

        resultado = converter_temperatura(temperatura, origem, destino)
        print(f"{temperatura} {origem.upper()} é igual a {resultado:.2f} {destino.upper()}")
    except ValueError as e:
        print(f"Erro: {e}")
    print("Fim do programa.")


if __name__ == "__main__":
    main()
