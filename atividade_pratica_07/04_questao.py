#!/usr/bin/python3
#-*-coding:utf-8-*-

import json

def ler_json(nome_arquivo):
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo_json:
            dados_json = json.load(arquivo_json)
            print(dados_json)
    except FileNotFoundError:
        return(f"Arquivo não encontrado")
    

def escrever_json(nome_arquivo, dados):
    try:
        with open(nome_arquivo, 'w', encoding='utf-8') as arquivo_json:
            json.dump(dados, arquivo_json, ensure_ascii = False, indent = 4)
        print(f"Dados salvos em: {nome_arquivo}")
    except Exception as e:
        return(f"Erro ao escrever no arquivo: {e}")
    
dados = {
    "nome": "John",
    "idade": 20,
    "cidade": "São Paulo"
}

nome_arquivo = input("Digite o nome do arquivo: ")
escrever_json(nome_arquivo, dados)
ler_json(nome_arquivo)