import constantes
from constantes import *
from termcolor import colored

# Lista de coordenadas de grupos
grupos_P = []
grupos_B = []


def controi_tabuleiro(tamanho):
    """
    construir o tabuleiro de Go para iniciar
    :param tamanho: Tamanho do tabuleiro de Go que foi solicitado
    :return: Matriz do tabeiro feita
    """

    tab = []
    for linhas in range(tamanho):
        coluna = []
        tab.append(coluna)
        if linhas >= 9:
            coluna.append("{} |".format(linhas + 1))
        else:
            coluna.append("{}  |".format(linhas + 1))
        for colunas in range(tamanho):
            if colunas == tamanho - 1:
                coluna.append(VAZIO)
                coluna.append(" |")
            else:
                coluna.append(VAZIO)

    return tab


def imprime_matriz(m, tamanho):
    """
    função de imprimir o tabubeiro
    Imprime a matriz do tabuleiro
    :param m: A matriz do tabuleiro a ser impresso
    :param tamanho: tamanha do tabuleiro
    """
    if tamanho == 9:
        print("      A  B  C  D  E  F  G  H  I")
    elif tamanho == 13:
        print("      A  B  C  D  E  F  G  H  I  J  K  L  M ")
    elif tamanho == 19:
        print("      A  B  C  D  E  F  G  H  I  J  K  L  M  N  O  P  Q  R  S ")

    for linha in range(len(m)):
        for coluna in range(len(m[linha])):
            if coluna == tamanho - 1:
                print(m[linha][coluna], end="")
            else:
                print(m[linha][coluna], end=" ")
        print()


def movimentando_tab(linha, coluna, tab, JOG, BOLA_BRANCA, BOLA_PRETA):
    """
    movimentação de Go na linha e na coluna que foi selecionado as peças
    :param linha:linha da matriz
    :param coluna: coluna da matriz
    :param tab: matriz
    :param JOG: Jogador
    :param BOLA_BRANCA:Peça Branca para identificar
    :param BOLA_PRETA: Peça Branca para identificar
    :return: O tabuleiro atualiza como a peça no local
    """

    if JOG == 0:
        tab[linha][coluna] = BOLA_PRETA

    elif JOG == 1:
        tab[linha][coluna] = BOLA_BRANCA


def interpretando_c(c):
    """
    interpretando as entradas de coluna que vão de A a S e substuindo por número interiro
    :param c: Coluna representada por Letras
    :return: retorna o número da coluna em inteiros
    """

    for i in range(len(letras_minusculas)):
        if c == letras_minusculas[i]:
            c = i + 1
            return c


def coordenadas(l, c, direcao):
    """
    função de pegar a direção e retornar as coordenadas da direção de verificação
    :param l: linha da matriz do tabuleiro
    :param c: coluna da matriz do tabuleiro
    :param direcao: Direção de verificação
    :return: retorna coordenadas de verificão
    """
    if direcao == "cima":
        return (l - 1, c)
    if direcao == "baixo":
        return (l + 1, c)
    if direcao == "esquerda":
        return (l, c - 1)
    if direcao == "direita":
        return (l, c + 1)


def verificando_se_he_grupo(tab, linha, coluna, tam):
    """
    verifica a cada movimento se formou um grupo verificando as direçãos das peças
    :param tab: Matriz da tabuleiro
    :param linha: linha da movimentação atual do tabeleiro
    :param coluna: Coluna da movimentação atual do tabeleiro
    :param tam: Tamanho da matriz do tabuleiro
    :return: As listas de grupos atualizadas com coordenadas de grupos
    """
    if linha < 2:
        cima = VAZIO
    else:
        cima = tab[linha - 1][coluna]
    if linha == tam - 1:
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
        if (cima in [VAZIO, " x", " Y", " |", PECA_BRANCA]) \
                and (baixo in [VAZIO, " x", " Y", " |", PECA_BRANCA]) \
                and (esquerda in [VAZIO, " x", " Y", " |", PECA_BRANCA]) \
                and (direita in [VAZIO, " x", " Y", " |", PECA_BRANCA]):
            grupos_P.append([])
            grupos_P[-1].append((linha, coluna))

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
        if (cima in [VAZIO, " x", " Y", " |", PECA_PRETA]) \
                and (baixo in [VAZIO, " x", " Y", " |", PECA_PRETA]) \
                and (esquerda in [VAZIO, " x", " Y", " |", PECA_PRETA]) \
                and (direita in [VAZIO, " x", " Y", " |", PECA_PRETA]):
            grupos_B.append([])
            grupos_B[-1].append((linha, coluna))

        cima_peca = coordenadas(linha, coluna, "cima")  # Posição da jogada
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
                    for item in grupos_B[index]:  # Pega todos os peças da lista atual e adiciona a primeira lista
                        grupos_B[primeiro].append((item[0], item[1]))
                    del grupos_B[index]  # Deleta a lista atual
                    index -= 1

            index += 1  # Atualiza o valor do index


def analisa_liberdade_grupo(tab, lista_grupos, jogador):
    """
    Verificas grupos se tem peças com liberdades livres se não houver chama
    função de captura e remove grupo da lista de grupo
    :param tab:Matriz do tabuleira para fazer verificação
    :param lista_grupos:Lista atual de grupos sendo analisada as liberdades
    :param jogador:Qual jogador vai pontuar se houver captura do grupo
    :return: captura ou não das peças
    """

    for grupo in lista_grupos:
        pecas_livres = []
        for peca in grupo:
            if peca_livre(tab, peca):
                pecas_livres.append(peca)

        if len(pecas_livres) == 0:
            captura(tab, grupo, jogador)
            lista_grupos.remove(grupo)


def peca_livre(tab, peca):
    """
    função que faz verificações das liberdades se tudo voltar false é por que não tem nenhuma liberdade
    se faltar alguma true é por que tem alguma liberdade
    :param tab:matriz para poder efetuar verificação
    :param peca:coordenada da matriz da peça sendo analisada no momento
    :return: retorna falso ou Verdaeiro se tem uma peça em cima , baixo , esquerda, direita
    """
    if peca[0] == 0:
        vizinho_cima = False
    else:
        vizinho_cima = tab[peca[0] - 1][peca[1]] != PECA_PRETA and tab[peca[0] - 1][peca[1]] != PECA_BRANCA
    if peca[0] == len(tab) - 1:
        vizinho_baixo = False
    else:
        vizinho_baixo = tab[peca[0] + 1][peca[1]] != PECA_PRETA and tab[peca[0] + 1][peca[1]] != PECA_BRANCA
    if peca[1] == 1:
        vizinho_esquerda = False
    else:
        vizinho_esquerda = tab[peca[0]][peca[1] - 1] != PECA_PRETA and tab[peca[0]][peca[1] - 1] != PECA_BRANCA
    if peca[1] == len(tab):
        vizinho_direita = False
    else:
        vizinho_direita = tab[peca[0]][peca[1] + 1] != PECA_PRETA and tab[peca[0]][peca[1] + 1] != PECA_BRANCA

    return vizinho_cima or vizinho_baixo or vizinho_esquerda or vizinho_direita


def captura(tab, grupo, jogador):
    """
    função que substitui coordanadas dos grupo em Vazio e da um acréscimo de quantidade de peças no contador
    :param tab:Matriz do tabuleiro
    :param grupo:Grupo de peças capturadas
    :param jogador:Jogador a ganhar os pontos da captura
    :return:retorna a lista da matriz autalizada sem as peças e contador atualizado
    """
    grupo = list(set(grupo))
    for peca in grupo:
        tab[peca[0]][peca[1]] = VAZIO
        if jogador == PECA_BRANCA:
            constantes.PONTOS_JOG2 += 1
        elif jogador == PECA_PRETA:
            constantes.PONTOS_JOG1 += 1


def condiz_fim_jogo(tab, tamanho):
    """
    verifica a condição de fim de jogo
    :param tab:Tabuleiro de go
    :param tamanho: tamanho da matriz do tabuleiro
    :return: [s] para parar o jogo e contar quem gangou [n] para continuar
    """
    meta = int(tamanho*tamanho*0.50)
    contador = 0
    for linha in range(len(tab)):
        for coluna in range(len(tab)):
            if tab[linha][coluna] in [PECA_PRETA, PECA_BRANCA]:
                contador += 1
    if contador >= meta:
        if contador >= int(tamanho*tamanho*0.65):
            print(colored("Devido ao tabuleiro estar muito preenchido o jogo irá acabar!!", "yellow"))
            return "s"
        else:
            pergunta = input(colored("Vocês gostariam de Acabar o jogo se sim[s] se não[n]?", "yellow")).lower()
            if pergunta not in ["s", "n"]:
                print(colored("fora do parametro a resposta tem que ser (s) ou (n)", "red"))
                condiz_fim_jogo(tab, tamanho)
            return pergunta


def quem_ganhou():
    """
    Função que calcula quem ganhou o jogo
    :return: quem ganhou
    """
    if constantes.PONTOS_JOG1 > constantes.PONTOS_JOG2:
        print("{} Ganhou!!".format(NOMES[0]))
    if constantes.PONTOS_JOG1 < constantes.PONTOS_JOG2:
        print("{} Ganhou!!".format(NOMES[1]))
    if constantes.PONTOS_JOG1 == constantes.PONTOS_JOG2:
        print("EMPATE!!")


def troca_turno(turno):
    """
    Troca os turnos dos jogadores
    :param turno: ha variavel turno que auxilia na troca de turnos
    :return: 0 para turno de preta e 1 para turno de branca
    """
    if (turno%2) == 0:
        constantes.TURNO += 1
        return 1
    else:
        constantes.TURNO += 1
        return 0