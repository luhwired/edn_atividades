#!/usr/bin/python3
#-*- coding:utf-8-*-

valor_reais = 100.00
taxa_dolar = 5.20
taxa_euro = 6.15

valor_dolar = valor_reais / taxa_dolar
valor_euro = valor_reais / taxa_euro

print(f'R$ {valor_reais:.2f} equivalem a:')
print(f'$ {valor_dolar:.2f} dólares')
print(f'€ {valor_euro:.2f} euros')
