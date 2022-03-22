from constantes import *

# contador
liberdades_pretas = []
liberdades_brancas = []
blocop = []
blocob = []
grupos_P = []
grupos_B = []


# contar liberdades e salvar coordenadas das peças em grupo
def contar_liberdades(tab):

    for linha in range(len(tab)):
        for coluna in range(len(tab)+1):
            quadrado = (linha, coluna)
            if linha != 0:
                cima = tab[linha - 1][coluna]
            else:
                cima = "xxxxxxxxx"
            if linha != len(tab) - 1:
                baixo = tab[linha + 1][coluna]
            else:
                baixo = "xxxxxxxx"
            esquerda = tab[linha][coluna - 1]
            direita = tab[linha][coluna + 1]

            if tab[linha][coluna] == PECA_PRETA or tab[linha][coluna] == PECA_BRANCA:

                if tab[linha][coluna] == PECA_PRETA:
                    if quadrado not in blocop:
                        blocop.append(quadrado)

                    if cima in [VAZIO, " x", " Y"]:
                        tab[linha - 1][coluna] = " x"
                        if cima not in liberdades_pretas:
                            liberdades_pretas.append(coordenadas(linha, coluna, "cima"))
                    if linha != len(tab) - 1:
                        if baixo in [VAZIO, " x", " Y"]:
                            tab[linha + 1][coluna] = " x"
                            if baixo not in liberdades_pretas:
                                liberdades_pretas.append(coordenadas(linha, coluna, "baixo"))

                    if esquerda in [VAZIO, " x", " Y"]:
                        tab[linha][coluna - 1] = " x"
                        if esquerda not in liberdades_pretas:
                            liberdades_pretas.append(coordenadas(linha, coluna, "esquerda"))

                    if direita in [VAZIO, " x", " Y"]:
                        tab[linha][coluna + 1] = " x"
                        if direita not in liberdades_pretas:
                            liberdades_pretas.append(coordenadas(linha, coluna, "direita"))

                else:
                    if quadrado not in blocob:
                        blocob.append(quadrado)

                    if cima in [VAZIO, " x", " Y"]:
                        tab[linha - 1][coluna] = " Y"
                        if cima not in liberdades_pretas:
                            liberdades_brancas.append(coordenadas(linha, coluna, "cima"))
                    if linha != len(tab) - 1:
                        if baixo in [VAZIO, " x", " Y"]:
                            tab[linha + 1][coluna] = " Y"
                            if baixo not in liberdades_pretas:
                                liberdades_brancas.append(coordenadas(linha, coluna, "baixo"))

                    if esquerda in [VAZIO, " x", " Y"]:
                        tab[linha][coluna - 1] = " Y"
                        if esquerda not in liberdades_pretas:
                            liberdades_brancas.append(coordenadas(linha, coluna, "esquerda"))

                    if direita in [VAZIO, " x", " Y"]:
                        tab[linha][coluna + 1] = " Y"
                        if direita not in liberdades_pretas:
                            liberdades_brancas.append(coordenadas(linha, coluna, "direita"))


def controi_tabuleiro(TAM):
    """construir o tabuleiro de Go para iniciar"""

    tab = []
    for linhas in range(TAM):
        coluna = []
        tab.append(coluna)
        if linhas >= 9:
            coluna.append(" {} |".format(linhas + 1))
        else:
            coluna.append("{}  |".format(linhas + 1))
        for colunas in range(TAM):
            if colunas == TAM-1:
                coluna.append(VAZIO)
                coluna.append(" |")
            else:
                coluna.append(VAZIO)

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
            if tab[linha][coluna] == PECA_PRETA or tab[linha][coluna] == PECA_BRANCA:

                if tab[linha][coluna] == PECA_PRETA:

                    if tab[linha - 1][coluna] == PECA_BRANCA or linha == 0:
                        cima = True
                    if linha == len(tab) - 1:
                        baixo = True
                    else:
                        if tab[linha + 1][coluna] == PECA_BRANCA or linha == len(tab):
                            baixo = True
                    if tab[linha][coluna - 1] == PECA_BRANCA or coluna == 1:
                        esqueda = True
                    if tab[linha][coluna + 1] == PECA_BRANCA or coluna == len(tab):
                        direita = True
                    if cima == True and baixo == True and esqueda == True and direita == True:
                        print("Achou Preta!!")
                        break
                else:
                    if tab[linha-1][coluna] == PECA_PRETA or linha == 0:
                        cima = True
                    if linha == len(tab) - 1:
                        baixo = True
                    else:
                        if tab[linha + 1][coluna] == PECA_BRANCA or linha == len(tab):
                            baixo = True
                    if tab[linha][coluna-1] == PECA_PRETA or coluna == 1:
                        esqueda = True
                    if tab[linha][coluna+1] == PECA_PRETA or coluna == len(tab):
                        direita = True
                    if cima == True and baixo == True and esqueda == True and direita == True:
                        print("Achou Branca!!")
                        break


def coordenadas(l, c, direcao):
    if direcao == "cima":
        return (l - 1 , c)
    if direcao == "baixo":
        return (l + 1, c)
    if direcao == "esquerda":
        return (l, c - 1)
    if direcao == "direita":
        return (l, c + 1)


def verificando_se_he_grupo(tab, linha, coluna, tam):
    if linha < 2:
        cima = VAZIO
    else:
        cima = tab[linha - 1][coluna]
    if linha == tam-1:
        baixo = VAZIO
    else:
        baixo = tab[linha + 1][coluna]
    if coluna < 2:
        esquerda = VAZIO
    else:
        esquerda = tab[linha][coluna - 1]
    if coluna == tam - 1:
        direita = VAZIO
    else:
        direita = tab[linha][coluna + 1]

    if tab[linha][coluna] == PECA_PRETA:
        if (cima in [VAZIO, " x", " Y", " |"])\
                and (baixo in [VAZIO, " x", " Y",  " |"])\
                and (esquerda in [VAZIO, " x", " Y", " |"])\
                and (direita in [VAZIO, " x", " Y", " |"]):
            grupos_P.append([])
            grupos_P[-1].append((linha, coluna))
        
        ########
        cima_peca = coordenadas(linha, coluna, "cima")  # Posição da jogada
        baixo_peca = coordenadas(linha, coluna, "baixo")
        esquerda_peca = coordenadas(linha, coluna, "esquerda")
        direita_peca = coordenadas(linha, coluna, "direita")

        primeiro = -1  # Index do primeiro item da lista que faz grupo com a peça adicionada
        ja_adicionou = False  # Verifica se a peça já foi adicionada a outra lista
        index = 0  # Index na lista de grupos
        
        while index < len(grupos_P):
            
            # Verifica se existe algum vizinho
            cima_peca_veri = cima_peca in grupos_P[index]
            baixo_peca_veri = baixo_peca in grupos_P[index]
            esquerda_peca_veri = esquerda_peca in grupos_P[index]
            direita_peca_veri = direita_peca in grupos_P[index]
            
            # Caso tenha vizinho
            if cima_peca_veri or baixo_peca_veri or esquerda_peca_veri or direita_peca_veri:
                if not ja_adicionou:  # Caso o item ainda não sido adicinado
                    grupos_P[index].append((linha, coluna))  # Adiciono ao grupo
                    primeiro = index  # Seta o index do primeiro grupo
                    ja_adicionou = True  # Seta o já adicionado
                    
                else:  # Caso o item já tenha sido adicionado
                    for item in grupos_P[index]:  # Pega todos os peças da lista atual e adiciona a primeira lista
                        grupos_P[primeiro].append((item[0], item[1]))
                    del grupos_P[index]  # Deleta a lista atual
                    index -= 1
                    
            index += 1  # Atualiza o valor do index

    elif tab[linha][coluna] == PECA_BRANCA:
        if (cima in [VAZIO, " x", " Y", " |"])\
                and (baixo in [VAZIO, " x", " Y", " |"])\
                and (esquerda in [VAZIO, " x", " Y", " |"])\
                and (direita in [VAZIO, " x", " Y", " |"]):
            grupos_B.append([])
            grupos_B[-1].append((linha, coluna))
            
        cima_peca = coordenadas(linha, coluna, "cima")  #Posição da jogada
        baixo_peca = coordenadas(linha, coluna, "baixo")
        esquerda_peca = coordenadas(linha, coluna, "esquerda")
        direita_peca = coordenadas(linha, coluna, "direita")
        
    
        primeiro = -1  # Index do primeiro item da lista que faz grupo com a peça adicionada
        ja_adicionou = False  # Verifica se a peça já foi adicionada a outra lista
        index = 0  # Index na lista de grupos
        
        while index < len(grupos_B):
            
            # Verifica se existe algum vizinho
            cima_peca_veri = cima_peca in grupos_B[index]
            baixo_peca_veri = baixo_peca in grupos_B[index]
            esquerda_peca_veri = esquerda_peca in grupos_B[index]
            direita_peca_veri = direita_peca in grupos_B[index]
            
            # Caso tenha vizinho
            if cima_peca_veri or baixo_peca_veri or esquerda_peca_veri or direita_peca_veri:
                if not ja_adicionou:  # Caso o item ainda não sido adicinado
                    grupos_B[index].append((linha, coluna))  # Adiciono ao grupo
                    primeiro = index  # Seta o index do primeiro grupo
                    ja_adicionou = True  # Seta o já adicionado
                    
                else:  # Caso o item já tenha sido adicionado
                    for item in grupos_B[index]:   # Pega todos os peças da lista atual e adiciona a primeira lista
                        grupos_B[primeiro].append((item[0], item[1]))
                    del grupos_B[index]   # Deleta a lista atual
                    index -= 1
                    
            index += 1  # Atualiza o valor do index
                           
        #######