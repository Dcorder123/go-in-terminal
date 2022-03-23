from jogo import *
from constantes import *


def tamanho_tabuleiro():
    print("Tamanho 9x9 {} Tamanho 13x13 {}\n Tamanho 19x19 {}".format(tab9, tab13, tab19))
    print()
    tamnaho_tabuleiro = input("Qual o tamanho que gotariam de jogar 9x9(9) ou 13x13(13) ou 19x19(19)? ")
    if tamnaho_tabuleiro != "9" and tamnaho_tabuleiro != "13" and tamnaho_tabuleiro != "19":
        print("Tamanho de tabuleiro errado!, por favor inserir tamanho de tabeleiro dentro das 3 opções")
        return tamanho_tabuleiro()

    else:
        TAM = int(tamnaho_tabuleiro)
        return TAM


def chamando_coluna_linha(tam, tab):
    """Nessa função iremos pedir a coluna e a linha iremos verificar se podemos fazer a jogada
    e se está dentro dos parametros"""

    letras = ["A", "B", "C",  "D",  "E ",  "F",  "G",  "H",  "I",  "J",  "K",  "L",  "M",  "N",  "O",  "P",  "Q",  "R", "S"]
    numeros = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19"]

    coluna = input("Qual coluna de A a {}? ".format(letras[tam - 1])).lower()

    if coluna not in letras_minusculas:
        print("Fora do parametro")
        imprime_matriz(e, tam)
        return chamando_coluna_linha(tam, tab)

    pego_linha = input("Qual linha de 1 a {}? ".format(tam))

    if pego_linha not in numeros:
        print("Tem que ser numeros positivos entre 1 e {}".format(tam))
        print("Ou ser Inteiro!")
        imprime_matriz(e, tam)
        return chamando_coluna_linha(tam, tab)
    linha = int(pego_linha)
    inter = interpretando_c(coluna)

    if inter > tam or linha > tam or inter < 0 or linha < 0:
        print("Posição fora do tabuleiro")
        print("Escolha outra posição")
        imprime_matriz(e, tam)
        return chamando_coluna_linha(tam, tab)
    if tab[linha - 1][inter] == PECA_PRETA or tab[linha - 1][inter] == PECA_BRANCA:
        print("Já tem uma peça nessa posição!")
        print(" Por favor escolher outra posição")
        imprime_matriz(e, tam)
        return chamando_coluna_linha(tam, tab)

    else:
        return inter, linha



# Inicia o jogo
TAM = tamanho_tabuleiro()
e = controi_tabuleiro(TAM)
imprime_matriz(e, TAM)

# Laço principal
while True:
    print("Vez de jogador 1!")
    coluna1, linha1 = chamando_coluna_linha(TAM, e)
    movimentando_tab(linha1 - 1, coluna1, e, JOG1, PECA_BRANCA, PECA_PRETA)
    contar_liberdades(e)
    verificando_se_he_grupo(e, linha1 - 1, coluna1, TAM)
    analisa_liberdade_grupo(e, grupos_B, PECA_PRETA)
    print("Pontos do Jogador 1: {} Pontos do Jogador 2: {}".format(PONTOS_JOG1, PONTOS_JOG2))
    imprime_matriz(e, TAM)
    lipamdo_liberdades()

    print("Vez de jogador 2!")
    coluna2, linha2 = chamando_coluna_linha(TAM, e)
    movimentando_tab(linha2 - 1, coluna2, e, JOG2, PECA_BRANCA, PECA_PRETA)
    contar_liberdades(e)
    verificando_se_he_grupo(e, linha2 - 1, coluna2, TAM)
    analisa_liberdade_grupo(e, grupos_P, PECA_BRANCA)
    print("Pontos do Jogador 1: {} Pontos do Jogador 2: {}".format(PONTOS_JOG1, PONTOS_JOG2))
    imprime_matriz(e, TAM)
    # print(blocop)
    # print(blocob)
    # print(liberdades_pretas)
    # print(liberdades_brancas)
    # print(grupos_P)
    # print(grupos_B)
    lipamdo_liberdades()
