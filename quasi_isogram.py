#!/usr/bin/env python3
import sys
# NOTE: it is recommended to use this even if you don't understand the following code.

#sys.stdin = open('quasi_input0.txt')
#sys.stdout = open('output.txt', 'w')
#input data
N = int(input().strip())


risposta = 0
for i in range(N):
    S = input().strip()
    Stringa= ""
    for i in range (0, len(S)):
        if S[i].isalpha():
            Stringa += S[i]
    Stringa =Stringa.lower()

    isogram = True
    contatori = {}
    for c in Stringa:
        if c not in contatori:
            contatori[c] = 1
        else:
            contatori[c] += 1 
        if contatori[c]> 2:
            isogram = False
            break

    if isogram:
        risposta += 1

    # insert your code here


print(risposta)  # print the result
