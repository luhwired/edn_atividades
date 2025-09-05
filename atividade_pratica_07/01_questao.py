#!/usr/bin/python3
#-*-coding:utf-8-*-

import pandas as pd

def processar_logs_treinamento(nome_arquivo):
    try:
        leitor = pd.read_csv(nome_arquivo)
        media_tempo = leitor['tempo_execucao'].mean()
        desvio_padrao = leitor['tempo_execucao'].std()
        return f"""
                Média do tempo de execução: {media_tempo}
                Desvio padrao do tempo de execução: {desvio_padrao:.2f}
                """
    except FileNotFoundError:
        return "Arquivo não encontrado."
    

nome_arquivo = input("Digite o nome do arquivo csv: ")

print(processar_logs_treinamento(nome_arquivo))