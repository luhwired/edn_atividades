#!/usr/bin/python3
#-*-coding:utf-8-*-

import requests

def gerar_perfil_usuario():
    url = "https://randomuser.me/api/"
    try:
        response = requests.get(url)
        response.raise_for_status() 
        dados = response.json()
        usuario = dados["results"][0]
        nome_completo = f"{usuario['name']['first']} {usuario['name']['last']}"
        email = usuario['email']
        pais = usuario['location']['country']

        print("\n--- Perfil de Usuário Gerado ---")
        print(f"Nome: {nome_completo}")
        print(f"Email: {email}")
        print(f"País: {pais}")
    except requests.exceptions.RequestException as e:
        print(f"Erro ao se conectar com a API: {e}")

gerar_perfil_usuario()