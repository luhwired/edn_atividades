#!/usr/bin/python3
#-*-coding:utf-8-*-

import requests

def consultar_cep(cep):
    cep_limpo = "".join(filter(str.isdigit, cep))
    
    if len(cep_limpo) != 8:
        print("Erro: O CEP deve conter 8 dígitos.")
        return

    url = f"https://viacep.com.br/ws/{cep_limpo}/json/"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        
        dados = response.json()

        if "erro" in dados:
            print(f"CEP {cep} não encontrado.")
        else:
            print("\n--- Endereço Encontrado ---")
            print(f"Logradouro: {dados.get('logradouro', 'N/A')}")
            print(f"Bairro: {dados.get('bairro', 'N/A')}")
            print(f"Cidade: {dados.get('localidade', 'N/A')}")
            print(f"Estado: {dados.get('uf', 'N/A')}")

    except requests.exceptions.RequestException as e:
        print(f"Erro ao consultar o CEP: {e}")

cep_usuario = input("Digite o CEP para consulta (apenas números): ")
consultar_cep(cep_usuario)