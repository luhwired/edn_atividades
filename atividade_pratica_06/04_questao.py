#!/usr/bin/python3
#-*-coding:utf-8-*-

import requests

def consultar_cotacao(codigo_moeda):
    par_moedas = f"{codigo_moeda.upper()}-BRL"
    url = f"https://economia.awesomeapi.com.br/json/last/{par_moedas}"

    try:
        response = requests.get(url)
        if response.status_code == 404:
            print(f"Erro: A moeda '{codigo_moeda.upper()}' não foi encontrada ou não é válida.")
            return

        response.raise_for_status()
        
        dados = response.json()
        chave_cotacao = par_moedas.replace('-', '')
        cotacao = dados[chave_cotacao]

        print(f"\n--- Cotação de {codigo_moeda.upper()}/BRL ---")
        print(f"Valor Atual (Compra): R$ {float(cotacao['bid']):.4f}")
        print(f"Máxima do Dia: R$ {float(cotacao['high']):.4f}")
        print(f"Mínima do Dia: R$ {float(cotacao['low']):.4f}")
        print(f"Última Atualização: {cotacao['create_date']}")

    except requests.exceptions.RequestException as e:
        print(f"Erro ao buscar cotação: {e}")
    except KeyError:
        print("Erro ao processar a resposta da API. Verifique o código da moeda.")

moeda = input("Digite o código da moeda para consulta (ex: USD, EUR, BTC): ")
consultar_cotacao(moeda)