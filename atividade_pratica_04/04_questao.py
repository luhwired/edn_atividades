#!/usr/bin/python3
# -*- coding: utf-8 -*-

def main():
    pares = impares = 0
    print("Digite números (digite 0 para encerrar).")
    
    while True:
        try:
            numero = int(input("Número: "))
            if numero == 0:
                break
            if numero % 2 == 0:
                pares += 1
                print(f"{numero} é par.")
            else:
                impares += 1
                print(f"{numero} é ímpar.")
        except ValueError:
            print("Entrada inválida. Digite apenas números inteiros.")
    
    print(f"Foram digitados {pares} números pares e {impares} números ímpares.")

if __name__ == "__main__":
    main()
