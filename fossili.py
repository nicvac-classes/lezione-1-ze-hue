#!/usr/bin/env python3

import sys

# se preferisci leggere e scrivere da file
# ti basta decommentare le seguenti due righe:

sys.stdin = open('fossili_input_1.txt')
sys.stdout = open('output.txt', 'w')


def solve(t):
    input()
    a1, a2 = map(int, input().strip().split())
    b1, b2 = map(int, input().strip().split())
    c1, c2 = map(int, input().strip().split())

    # aggiungi codice...
    estinto=min(a2,c2,b2)
    comparsi=max(a1,b1,c1)
    risposta = estinto-comparsi

    print(f"Case #{t}: {risposta}")




T = int(input().strip())

for t in range(1, T+1):
    solve(t)

sys.stdout.close()
