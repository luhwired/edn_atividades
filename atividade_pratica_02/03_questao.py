#!/usr/bin/python3
#-*-coding:utf-8-

nota1 = 7.5
nota2 = 8.0
nota3 = 6.5

soma = 0
for nota in range(0,3):
    nota = float(input("Informe sua nota:"))
    soma += nota

media = soma / 3
print(f"A média das notas é: {media:.1f}")
