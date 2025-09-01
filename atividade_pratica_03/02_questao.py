#!/usr/bin/python3
# -*- coding: utf-8 -*-

def calcular_imc(peso: float, altura: float) -> tuple[float, str]:
    """Calcula o IMC e retorna o valor e a classificação."""
    imc = peso / (altura ** 2)

    if imc < 18.5:
        classificacao = "Abaixo do peso"
    elif imc < 25:
        classificacao = "Peso normal"
    elif imc < 30:
        classificacao = "Sobrepeso"
    else:
        classificacao = "Obeso"
    
    return imc, classificacao


def main():
    try:
        peso = float(input("Digite o seu peso em kg: "))
        altura = float(input("Digite a sua altura em metros: "))

        imc, classificacao = calcular_imc(peso, altura)
        print(f"Seu IMC é {imc:.1f} e você está classificado como {classificacao}.")
    except ValueError:
        print("Entrada inválida! Digite apenas números.")
    except ZeroDivisionError:
        print("A altura não pode ser zero.")

    print("Fim do programa.")


if __name__ == "__main__":
    main()
