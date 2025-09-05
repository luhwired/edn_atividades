#!/usr/bin/python3
#-*-coding:utf-8-*-

import csv

def ler_csv(nome_arquivo):
    try:
        with open(nome_arquivo, 'r', newline='', encoding='utf-8') as arquivo_csv:
            leitor = csv.reader(arquivo_csv)
            for linha in leitor:
                print(linha)
    except FileNotFoundError:
        return(f"Arquivo não encontrado")

nome_arquivo = input("Digite o nome do arquivo: ")
print(ler_csv(nome_arquivo))