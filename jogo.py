from constantes import *

# contador
liberdades_pretas = []
liberdades_brancas = []
blocop = []
blocob = []
grupos = []

# contar liberdades e salvar coordenadas das peças em grupo
def contar_liberdades(tab, TAM):

    count = 8
    count2 = 8
    for linha in range(len(tab)):
        for coluna in range(len(tab)+1):
            quadrado = (linha, coluna)

            if tab[linha][coluna] == BOLA_PRETA or tab[linha][coluna] == BOLA_BRANCA:

                if tab[linha][coluna] == BOLA_PRETA:
                    if quadrado not in blocop:
                        blocop.append(quadrado)

                    if tab[linha - 1][coluna] == BOLA_BRANCA or linha == 0:
                        count -= 1
                    else:
                        if tab[linha - 1][coluna] == BOLA_PRETA:
                            count += 1
                        else:
                            if tab[linha - 1][coluna] == BOLA_BRANCA:
                                count += 1
                            else:
                                if tab[linha - 1][coluna] == BOLA_PRETA:
                                    count -= 1
                                else:
                                    tab[linha - 1][coluna] = " x"
                                    cima = (linha - 1, coluna)
                                    if cima not in liberdades_pretas:
                                        liberdades_pretas.append(cima)

                    if linha == len(tab) - 1:
                        count -= 1
                    else:
                        if tab[linha + 1][coluna] == BOLA_PRETA or linha == len(tab) - 1:
                            count -= 1
                        else:
                            if tab[linha + 1][coluna] == BOLA_PRETA:
                                count += 1
                            else:
                                if tab[linha + 1][coluna] == BOLA_BRANCA:
                                    count -= 1
                                else:
                                    tab[linha + 1][coluna] = " x"
                                    baixo = (linha + 1, coluna)
                                    if baixo not in liberdades_pretas:
                                        liberdades_pretas.append(baixo)

                    if tab[linha][coluna - 1] == BOLA_BRANCA or coluna == 1:
                        count -= 1
                    else:
                        if tab[linha][coluna - 1] == BOLA_PRETA:
                            count += 1
                        else:
                            if tab[linha][coluna - 1] == BOLA_BRANCA:
                                count -= 1
                            else:
                                tab[linha][coluna - 1] = " x"
                                esquerdo = (linha, coluna - 1)
                                if esquerdo not in liberdades_pretas:
                                    liberdades_pretas.append(esquerdo)
                    if tab[linha][coluna + 1] == BOLA_BRANCA or coluna == len(tab):
                        count -= 1
                    else:
                        if tab[linha][coluna + 1] == BOLA_PRETA:
                            count += 1
                        else:
                            if tab[linha][coluna + 1] == BOLA_BRANCA:
                                count -= 1
                            else:
                                tab[linha][coluna + 1] = " x"
                                direita = (linha, coluna + 1)
                                if direita not in liberdades_pretas:
                                    liberdades_pretas.append(direita)
                else:
                    if quadrado not in blocob:
                        blocob.append(quadrado)

                    if tab[linha - 1][coluna] == BOLA_PRETA or linha == 0:
                        count2 -= 1
                    else:
                        if tab[linha - 1][coluna] == BOLA_BRANCA:
                            count2 += 1
                        else:
                            if tab[linha - 1][coluna] == BOLA_PRETA:
                                count2 += 1
                            else:
                                tab[linha - 1][coluna] = " Y"
                                baixo = (linha - 1, coluna)
                                if baixo not in liberdades_pretas:
                                    liberdades_brancas.append(baixo)

                    if linha == len(tab)-1:
                        count2 -= 1
                    else:
                        if tab[linha + 1][coluna] == BOLA_PRETA or linha == len(tab) - 1:
                            count2 -= 1
                        else:
                            if tab[linha + 1][coluna] == BOLA_BRANCA:
                                count2 += 1
                            else:
                                if tab[linha + 1][coluna] == BOLA_PRETA:
                                    count2 += 1
                                else:
                                    tab[linha + 1][coluna] = " Y"
                                    cima = (linha + 1, coluna)
                                    if cima not in liberdades_pretas:
                                        liberdades_brancas.append(cima)

                    if tab[linha][coluna - 1] == BOLA_PRETA or coluna == 1:
                        count2 -= 1
                    else:
                        if tab[linha][coluna - 1] == BOLA_BRANCA:
                            count2 += 1
                        else:
                            if tab[linha][coluna - 1] == BOLA_PRETA:
                                count2 += 1
                            else:
                                tab[linha][coluna - 1] = " Y"
                                esquerdo = (linha, coluna - 1)
                                if esquerdo not in liberdades_pretas:
                                    liberdades_brancas.append(esquerdo)

                    if tab[linha][coluna + 1] == BOLA_PRETA or coluna == len(tab):
                        count2 -= 1
                    else:
                        if tab[linha][coluna + 1] == BOLA_BRANCA:
                            count2 += 1
                        else:
                            if tab[linha][coluna + 1] == BOLA_PRETA:
                                count2 += 1
                            else:
                                tab[linha][coluna + 1] = " Y"
                                direita = (linha, coluna + 1)
                                if direita not in liberdades_pretas:
                                    liberdades_brancas.append(direita)


def controi_tabuleiro(TAM):
    """construir o tabuleiro de Go para iniciar"""

    tab = []
    for linhas in range(TAM):
        coluna = []
        tab.append(coluna)
        if linhas >= 9:
            coluna.append("{} |".format(linhas + 1))
        else:
            coluna.append("{}  |".format(linhas + 1))
        for colunas in range(TAM):
            if colunas == TAM-1:
                coluna.append(" .")
                coluna.append(" |")
            else:
                coluna.append(" .")

    return tab


def imprime_matriz(m, tam):
    """
    Imprime um tabuleiro
    :param m: o tabuleiro a ser impresso
    """
    if tam == 9:
        print("      A  B  C  D  E  F  G  H  I")
    elif tam == 13:
        print("      A  B  C  D  E  F  G  H  I  J  K  L  M ")
    elif tam == 19:
        print("      A  B  C  D  E  F  G  H  I  J  K  L  M  N  O  P  Q  R  S ")

    for linha in range(len(m)):
        for coluna in range(len(m[linha])):
            if coluna == tam - 1:
                print(m[linha][coluna], end="")
            else:
                print(m[linha][coluna], end=" ")
        print()


def movimentando_tab(linha, coluna, tab, JOG, BOLA_BRANCA, BOLA_PRETA):
    """movimentação de Go na linha e na coluna que foi selecionado as peças"""

    if JOG == 1:
        tab[linha][coluna] = BOLA_PRETA

    elif JOG == 2:
        tab[linha][coluna] = BOLA_BRANCA


def interpretando_c(c):
    """interpretando as entradas de coluna que vão de A a S e substuindo por número interiro"""

    for i in range(len(letras_minusculas)):
        if c == letras_minusculas[i]:
            c = i + 1
            return c


def capturando_innimigo(tab):

    for linha in range(len(tab)):
        cima = False
        baixo = False
        esqueda = False
        direita = False

        for coluna in range(len(tab)):
            if tab[linha][coluna] == BOLA_PRETA or tab[linha][coluna] == BOLA_BRANCA:

                if tab[linha][coluna] == BOLA_PRETA:

                    if tab[linha - 1][coluna] == BOLA_BRANCA or linha == 0:
                        cima = True
                    if linha == len(tab) - 1:
                        baixo = True
                    else:
                        if tab[linha + 1][coluna] == BOLA_BRANCA or linha == len(tab):
                            baixo = True
                    if tab[linha][coluna - 1] == BOLA_BRANCA or coluna == 1:
                        esqueda = True
                    if tab[linha][coluna + 1] == BOLA_BRANCA or coluna == len(tab):
                        direita = True
                    if cima == True and baixo == True and esqueda == True and direita == True:
                        print("Achou Preta!!")
                        break
                else:
                    if tab[linha-1][coluna] == BOLA_PRETA or linha == 0:
                        cima = True
                    if linha == len(tab) - 1:
                        baixo = True
                    else:
                        if tab[linha + 1][coluna] == BOLA_BRANCA or linha == len(tab):
                            baixo = True
                    if tab[linha][coluna-1] == BOLA_PRETA or coluna == 1:
                        esqueda = True
                    if tab[linha][coluna+1] == BOLA_PRETA or coluna == len(tab):
                        direita = True
                    if cima == True and baixo == True and esqueda == True and direita == True:
                        print("Achou Branca!!")
                        break


def verificando_se_he_grupo(tab):

    for linha in range(len(tab)):
        cima1 = False
        baixo1 = False
        esqueda1 = False
        direita1 = False

        for coluna in range(len(tab)):
            cima = tab[linha - 1][coluna]
            baixo = tab[linha + 1][coluna]
            esqueda = tab[linha][coluna - 1]
            direita = tab[linha][coluna + 1]
            if tab[linha][coluna] == BOLA_PRETA:


                if cima == BOLA_BRANCA or linha == 0:
                    grupos.append((linha, coluna))

                if linha == len(tab) - 1:

                    baixo1 = True
                else:
                    if baixo == BOLA_BRANCA or linha == len(tab):
                        baixo1 = True
                if esqueda == BOLA_BRANCA or coluna == 1:
                    esqueda1 = True
                if direita == BOLA_BRANCA or coluna == len(tab):
                    direita1 = True

            else:
                if cima == BOLA_PRETA or linha == 0:
                    cima1 = True
                if linha == len(tab) - 1:
                    baixo1 = True
                else:
                    if baixo == BOLA_BRANCA or linha == len(tab):
                        baixo1 = True
                if esqueda == BOLA_PRETA or coluna == 1:
                    esqueda1 = True
                if direita == BOLA_PRETA or coluna == len(tab):
                    direita1 = True
