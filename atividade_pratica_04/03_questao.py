#!/usr/bin/python3
# -*- coding: utf-8 -*-

def verificar_senha(senha: str) -> bool:
    """Verifica se a senha atende aos critérios básicos de segurança."""
    tem_tamanho = len(senha) >= 8
    tem_numero = any(ch.isdigit() for ch in senha)

    return tem_tamanho and tem_numero

def main():
    senha = input("Digite a senha: ")

    if verificar_senha(senha):
        print("Senha válida!")
    else:
        print("Senha inválida! Deve ter pelo menos 8 caracteres e conter ao menos um número.")

    print("Fim do programa.")

if __name__ == "__main__":
    main()
