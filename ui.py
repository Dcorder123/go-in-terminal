from jogo import *
from constantes import *
from termcolor import colored


def tamanho_tabuleiro():
    """
    Função que chama o tamanho do tabuleiro e se for tamanho fora dos parametros chama de novo
    a função
    :return: tamanho do tabuleiro
    """
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
    """
    Nessa função iremos pedir a coluna e a linha iremos verificar se podemos fazer a jogada
    e se está dentro dos parametros
    :param tam:Tamanho da Matriz do tabuleiro
    :param tab: Matriz do tabeleiro
    :return: linha e coluna corretas para a movimentação e também menssagens de erros quando errada
    """

    letras = ["A", "B", "C",  "D",  "E ",  "F",  "G",  "H",  "I",  "J",  "K",  "L",  "M",  "N",  "O",  "P",  "Q",  "R", "S"]
    numeros = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19"]

    coluna = input("Qual coluna de A a {}? ".format(letras[tam - 1])).lower()

    if coluna not in letras_minusculas:
        print(colored("Fora do parametro", "red"))
        imprime_matriz(tabuleiro, tam)
        return chamando_coluna_linha(tam, tab)

    pego_linha = input("Qual linha de 1 a {}? ".format(tam))

    if pego_linha not in numeros:
        print(colored("Tem que ser numeros positivos entre 1 e {}".format(tam), "red"))
        print(colored("Ou ser Inteiro!", "red"))
        imprime_matriz(tabuleiro, tam)
        return chamando_coluna_linha(tam, tab)
    linha = int(pego_linha)
    inter = interpretando_c(coluna)

    if inter > tam or linha > tam or inter < 0 or linha < 0:
        print(colored("Posição fora do tabuleiro", "red"))
        print(colored("Escolha outra posição!!", "red"))
        imprime_matriz(tabuleiro, tam)
        return chamando_coluna_linha(tam, tab)
    if tab[linha - 1][inter] == PECA_PRETA or tab[linha - 1][inter] == PECA_BRANCA:
        print(colored("Já tem uma peça nessa posição!", "red"))
        print(colored("Por favor escolher outra posição", "red"))
        imprime_matriz(tabuleiro, tam)
        return chamando_coluna_linha(tam, tab)

    else:
        return inter, linha



# Inicia o jogo
nome_jog1 = input("Nome de Jogador 1: ")
NOMES.append(nome_jog1)
nome_jog2 = input("Nome de Jogador 2: ")
NOMES.append(nome_jog2)
TAM = tamanho_tabuleiro()
tabuleiro = controi_tabuleiro(TAM)
imprime_matriz(tabuleiro, TAM)

# Laço principal
while True:
    print(colored("Vez de {}! {}", "blue").format(NOMES[0], "(Cor Preta)"))
    coluna1, linha1 = chamando_coluna_linha(TAM, tabuleiro)
    movimentando_tab(linha1 - 1, coluna1, tabuleiro, JOG1, PECA_BRANCA, PECA_PRETA)
    verificando_se_he_grupo(tabuleiro, linha1 - 1, coluna1, TAM)
    analisa_liberdade_grupo(tabuleiro, grupos_B, PECA_PRETA)
    print("Pontos do Jogador 1: {} \nPontos do Jogador 2: {}".format(constantes.PONTOS_JOG1, constantes.PONTOS_JOG2))
    imprime_matriz(tabuleiro, TAM)

    print(colored("Vez de {}! {}", "green").format(NOMES[1], "(Cor Branca)"))
    coluna2, linha2 = chamando_coluna_linha(TAM, tabuleiro)
    movimentando_tab(linha2 - 1, coluna2, tabuleiro, JOG2, PECA_BRANCA, PECA_PRETA)
    verificando_se_he_grupo(tabuleiro, linha2 - 1, coluna2, TAM)
    analisa_liberdade_grupo(tabuleiro, grupos_P, PECA_BRANCA)
    print("Pontos do Jogador 1: {}\nPontos do Jogador 2: {}".format(constantes.PONTOS_JOG1, constantes.PONTOS_JOG2))
    imprime_matriz(tabuleiro, TAM)

