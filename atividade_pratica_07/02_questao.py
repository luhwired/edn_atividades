#!/usr/bin/python3
#-*-coding:utf-8-*-

import csv

cabecalho = ['Nome', 'Idade', 'Cidade']
dados = [
    ['Ana', 28, 'São Paulo'],
    ['Bruno', 35, 'Recife'],
    ['Carla', 22, 'Boa Vista'],
    ['Daniel', 41, 'Manaus']
]

nome_arquivo = 'pessoas.csv'

try:
    with open(nome_arquivo, 'w', newline='', encoding='utf-8') as arquivo_csv:
        escritor_csv = csv.writer(arquivo_csv)
        escritor_csv.writerow(cabecalho)
        escritor_csv.writerows(dados)

    print(f"Arquivo '{nome_arquivo}' foi criado com sucesso!")

except IOError:
    print(f"Não foi possível escrever no arquivo '{nome_arquivo}'. Verifique as permissões.")