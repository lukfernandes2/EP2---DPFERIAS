import random

# PARA TESTAS O SEU CÓDIGO NA ACADEMIA PYTHON SERÁ NECESSÁRIO COLAR AS FUNÇÕES DESENVOLVIDAS AQUI!!!

from funcoes import *

# Gerando frota de forma aleatório para jogadores
frota_jogador = gerando_frota_automaticamente()
frota_oponente = gerando_frota_automaticamente()

# Criando tabuleiro com as frotas posicionadas
tabuleiro_jogador = posiciona_frota(frota_jogador)
tabuleiro_oponente = posiciona_frota(frota_oponente)

jogando = True


lista_ataque = [["", ""]]
coordenada = ["", ""]
lista_ataque_oponente = [["", ""]]
coordenada_oponente = ["", ""]

while jogando:

    # Imprimindo tabuleiro
    print(monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente))

    # TODO: Implemente aqui a lógica para perguntar a linha que o jogador deseja atirar
    while coordenada in lista_ataque:

        lista_ataque.append(coordenada)

        verificando_linha = True
        while verificando_linha:
            linha = int(input("Qual linha você deseja atacar?"))

            if linha < 0 or linha > 9:

                print("Linha inválida!")

                linha = int(input("Qual linha você deseja atacar?"))

            else:
                verificando_linha = False

        verificando_coluna = True
        while verificando_coluna:
            coluna = int(input("Qual linha você deseja atacar?"))

            if coluna < 0 or coluna > 9:

                print("Coluna inválida!")

                coluna = int(input("Qual coluna você deseja atacar?"))

            else:
                verificando_coluna = False

        coordenada = [linha, coluna]

        if coordenada in lista_ataque:

            print(f"A posição linha {linha} e coluna {coluna} já foi informada anteriormente!")

        else:
            lista_ataque.append(coordenada)

            tabuleiro_oponente = faz_jogada(tabuleiro_oponente, linha, coluna)
            
            navios_afundados = afundados(frota_oponente, tabuleiro_oponente)

            if navios_afundados == len(frota_oponente):

                print('Parabéns! Você derrubou todos os navios do seu oponente!')

                jogando = False

            break

    while coordenada_oponente in lista_ataque_oponente:

        lista_ataque_oponente.append(coordenada_oponente)

        linha_oponente = random.randint(0,9)

        coluna_oponente = random.randint(0,9)

        coordenada_oponente = [linha_oponente, coluna_oponente]

        if coordenada_oponente not in lista_ataque_oponente:

            lista_ataque_oponente.append(coordenada_oponente)

            tabuleiro_jogador = faz_jogada(tabuleiro_jogador, linha_oponente, coluna_oponente)

            if jogando == True:
                print(f"Seu oponente está atacando na linha {linha_oponente} e coluna {coluna_oponente}")
            
            navios_afundados_oponente = afundados(frota_jogador, tabuleiro_jogador)

            if navios_afundados_oponente == len(frota_jogador):

                print('Xi! O oponente derrubou toda a sua frota')

                jogando = False

            break
    