#!/usr/bin/python3
# -*- coding: utf-8 -*-

def eh_bissexto(ano: int) -> bool:
    """Verifica se um ano é bissexto."""
    return ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0)


def main():
    try:
        ano = int(input("Digite um ano: "))
        if eh_bissexto(ano):
            print(f"{ano} é bissexto")
        else:
            print(f"{ano} não é bissexto")
    except ValueError:
        print("Entrada inválida! Digite apenas números inteiros.")
    
    print("Fim do programa.")


if __name__ == "__main__":
    main()
