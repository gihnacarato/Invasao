# Solução: a Invasão

# Funções

from cgi import print_environ


def preencheN(n):
    Ln = []
    for i in range(n):
        y = int(input('n[%d]: ' % (i)))
        Ln.append(y)
    return Ln


def somaM(L):
    sm = 0
    m = len(L)
    for i in range(m):
        sm += L[i]
    return sm


def somaD(sm):
    dmd = 0
    sd = 0
    while sm > 0:
        dmd = sm % 10
        sd += dmd
        sm = sm // 10
    return sd


def trocaN(L, i, j):
    x = L[i]
    L[i] = L[j]
    L[j] = x


def ordenaN(L):
    n = len(L)
    for i in range(n, 1, -1):
        m = selecionaN(L, i)
        trocaN(L, m, i-1)
    return L


def selecionaN(L, n):
    m = 0
    for i in range(1, n):
        if L[i] > L[m]:
            m = i
    return m


def multiplicaN(L):
    sn = 0
    n = len(L)
    j = 1
    i = 0
    while i <= n and j <= n:
        sn += L[i] * j
        j += 1
        i += 1
    return sn


def geraSeq(n):
    L = []
    x = 1
    j = 0
    for i in range(0, n):
        x += j
        L.append(x)
        j += 1
    return L


def somaSeqN(Ln, seq):
    Lsoma = []
    n = len(Ln)
    for i in range(0, n):
        Lsoma.append(Ln[i] + seq[i])
    return Lsoma


def geraSN(Ln):
    dmd = 0
    dmd2 = 0
    sn = 0
    n = len(Ln)
    for i in range(0, n):
        dmd = Ln[i] % 100
        dmd2 = dmd % 10
        dmd = dmd // 10
        sn += dmd2
        sn += dmd
    return sn


def defineData(dia, mes):
    if mes == 1 and dia <= 31:
        mes = "Janeiro"
    elif mes == 2 and dia <= 28:
        mes = "Fevereiro"
    elif mes == 3 and dia <= 31:
        mes = "Março"
    elif mes == 4 and dia <= 30:
        mes = "Abril"
    elif mes == 5 and dia <= 31:
        mes = "Maio"
    elif mes == 6 and dia <= 30:
        mes = "Junho"
    elif mes == 7 and dia <= 31:
        mes = "Julho"
    elif mes == 8 and dia <= 31:
        mes = "Agosto"
    elif mes == 9 and dia <= 30:
        mes = "Setembro"
    elif mes == 10 and dia <= 31:
        mes = "Outubro"
    elif mes == 11 and dia <= 30:
        mes = "Novembro"
    elif mes == 12 or mes == 0 and dia <= 31:
        mes = "Dezembro"
    else:
        return "Código corrompido"

    return "Invasão: %d de %s" % (dia, mes)


# Entrada de Dados e declaração de variáveis
i = 0
m = int(input('Entre com m: '))
n = int(input('Entre com n: '))
error = False
Lm = []
seq = []

# Validação da entrada M e N
if 0 < m < 6 and 0 < n < 11:
    while i < m and error == False:
        x = int(input('m[%d]: ' % (i)))
        i += 1
        if 0 < x < 500:
            Lm.append(x)
        else:
            print('Código corrompido!!!')
            error = True

    if error == False:
        Ln = preencheN(n)

     # Soma dos valores de M e digitos de SM

    sm = somaM(Lm)
    sd = somaD(sm)

    # Verificação de qual metodo usar
    if sd % 2 == 0:
        print("Método A")
        Ln = ordenaN(Ln)
        sn = multiplicaN(Ln)

    else:
        print("Método B")
        seq = geraSeq(n)
        Lsoma = somaSeqN(Ln, seq)
        sn = geraSN(Lsoma)

    # Descobrindo a data
    dia = sn % 31
    if dia > 0:
        mes = sn % 12
        data = defineData(dia, mes)
        print(data)
    else:
        print('Código corrompido!!!')

else:
    print('Código corrompido!!!')
