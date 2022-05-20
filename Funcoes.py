from random import randint
import re


def preenche():
    L = []
    for i in range(5):
        L.append(int(input("Valor: ")))
    return L


def aleatoria(n):
    L = []
    for i in range(n):
        L.append(randint(10, 99))
    return L


def troca(L, i, j):
    x = L[i]
    L[i] = L[j]
    L[j] = x


def selection_sort(L):
    n = len(L)
    cresN = []
    for i in range(n, 1, -1):
        m = seleciona(L, i)
        cresN.append(troca(L, m, i-1))
    return cresN


def seleciona(L, n):
    m = 0
    for i in range(1, n):
        if L[i] > L[m]:
            m = 1
    return m


def ordenada(L):
    for i in range(0, n - 1):
        if L[i] > L[i + 1]:
            return False
        return True


def somaM(L, m):
    sm = 0
    for i in range(m):
        sm += L[i]


def somaD(sm):
    dmd = 0
    sd = 0
    while sm > 0:
        dmd = sm % 10
        sd += dmd
        sm = sm // 10
    print(sd)


def metodoA(L):
    maior = 0
    n = len(L)
    cresL = []
    for i in range(1, n):
        if L[i] > maior:
            aux = L[i]
            cresL.append(aux)
    return cresL


s = 123456789 % 100
print(s)
