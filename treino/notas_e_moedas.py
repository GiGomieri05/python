# -*- coding: utf-8 -*-

N = float(input())  # Valor em reais

notas = [100.0, 50.0, 20.0, 10.0, 5.0, 2.0]
moedas = [1.0, 0.5, 0.25, 0.10, 0.05, 0.01]

# Converter para centavos para evitar problemas com ponto flutuante
centavos = round(N * 100)

print("NOTAS:")
for nota in notas:
    valor_nota = int(nota * 100)  # Valor da nota em centavos
    quantidade = centavos // valor_nota
    print(f"{quantidade} nota(s) de R$ {nota:.2f}")
    centavos %= valor_nota

print("MOEDAS:")
for moeda in moedas:
    valor_moeda = int(moeda * 100)  # Valor da moeda em centavos
    quantidade = centavos // valor_moeda
    print(f"{quantidade} moeda(s) de R$ {moeda:.2f}")
    centavos %= valor_moeda
