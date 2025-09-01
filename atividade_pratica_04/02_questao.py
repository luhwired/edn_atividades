#!/usr/bin/python3
# -*- coding: utf-8 -*-

def calcular_media(notas: list[float]) -> float:
    """Calcula a média de uma lista de notas."""
    return sum(notas) / len(notas) if notas else 0.0

def main():
    try:
        qtd = int(input("Digite a quantidade de alunos: "))
        notas = []
        for i in range(qtd):
            nota = float(input(f"Digite a nota do aluno {i+1}: "))
            notas.append(nota)

        media = calcular_media(notas)
        print(f"A média da turma é: {media:.2f}")
    except Exception as e:
        print(f"Erro: {e}")

    print("Fim do programa.")

if __name__ == "__main__":
    main()
