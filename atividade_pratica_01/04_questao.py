#!/usr/bin/python3
#-*-coding:utf-8-*-

nome_do_produto = "Cadeira Infantil"
preco_unitario = 12.40
quantidade = 3

preco_total = preco_unitario * quantidade

print(f"Produto: {nome_do_produto}")
print(f"Preço unitário: R$ {preco_unitario}")
print(f"Quantidade: {quantidade}")
print(f"Preço total: R$ {preco_total:.2f}")
