import random

# PARA TESTAS O SEU CÓDIGO NA ACADEMIA PYTHON SERÁ NECESSÁRIO COLAR AS FUNÇÕES DESENVOLVIDAS AQUI!!!

from funcoes import *

def monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente):
    '''
    tabuleiro_jogador: tabuleiro do jogador
    tabuleiro_oponente: tabuleiro do oponente
    Função monta uma string com a representação dos tabuleiros do jogador e do oponente.
    O tabuleiro do jogador é representado por um tabuleiro com as posições dos navios.

    
    O tabuleiro do oponente é representado por um tabuleiro com as posições que o jogador já atirou.
    '''

    texto = ''
    texto += '   0  1  2  3  4  5  6  7  8  9         0  1  2  3  4  5  6  7  8  9\n'
    texto += '_______________________________      _______________________________\n'

    for linha in range(len(tabuleiro_jogador)):
        jogador_info = '  '.join([str(item)
                                  for item in tabuleiro_jogador[linha]])
        oponente_info = '  '.join(
            [info if str(info) in 'X-' else '0' for info in tabuleiro_oponente[linha]])
        texto += f'{linha}| {jogador_info}|     {linha}| {oponente_info}|\n'
    texto += '_______________________________      _______________________________\n'
    return texto


def gerando_frota_automaticamente():
    '''
    Função gera uma frota de navios de forma aleatória.
    '''
    quantidades = {
        "submarino": {
            "quantidade": 4,
            "tamanho": 1
        },
        "destroyer": {
            "quantidade": 3,
            "tamanho": 2
        },
        "navio-tanque": {
            "quantidade": 2,
            "tamanho": 3
        },
        "porta-aviões": {
            "quantidade": 1,
            "tamanho": 4
        }
    }

    frota = []

    for nome_navio, info in quantidades.items():
        for _ in range(info["quantidade"]):
            dados_de_posicionamento = {
                "tamanho": info["tamanho"],
            }
            dados_de_posicionamento["orientacao"] = random.choice(
                ["vertical", "horizontal"])
            dados_de_posicionamento["linha"] = random.randint(0, 9)
            dados_de_posicionamento["coluna"] = random.randint(0, 9)

            while not posicao_valida(dados_de_posicionamento, frota):
                dados_de_posicionamento["orientacao"] = random.choice(
                    ["vertical", "horizontal"])
                dados_de_posicionamento["linha"] = random.randint(0, 9)
                dados_de_posicionamento["coluna"] = random.randint(0, 9)

            preenche_frota(dados_de_posicionamento, nome_navio, frota)

    return frota


# Gerando frota de forma aleatório para jogadores
frota_jogador = gerando_frota_automaticamente()
frota_oponente = gerando_frota_automaticamente()

# Criando tabuleiro com as frotas posicionadas
tabuleiro_jogador = posiciona_frota(frota_jogador)
tabuleiro_oponente = posiciona_frota(frota_oponente)
jogando = True
while jogando:

    # Imprimindo tabuleiro
    print(monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente))

    # TODO: Implemente aqui a lógica para perguntar a linha que o jogador deseja atirar

    lista_ataque = []

    linha = 0

    coluna = 0

    coordenada = [linha, coluna]
    
    while coordenada not in lista_ataque:
    
        linha = int(input("Qual linha você deseja atacar?"))

        while linha < 0 or linha > 9:

            print("Linha inválida!")

            linha = int(input("Qual linha você deseja atacar?"))

        coluna = int(input("Qual coluna você deseja atacar?"))

        while coluna < 0 or coluna > 9:

            print("Linha inválida!")

            coluna = int(input("Qual coluna você deseja atacar?"))
        
        coordenada = [linha, coluna]

        if coordenada in lista_ataque:

            print(f"A posição linha {linha} e coluna {coluna} já foi informada anteriormente!")
        
        else:

            tabuleiro_oponente = faz_jogada(tabuleiro_oponente, linha, coluna)

            lista_ataque.append(coordenada)
        
        navios_afundados = afundados(frota_oponente, tabuleiro_oponente)

        if navios_afundados == len(frota_oponente):

            print('Parabéns! Você derrubou todos os navios do seu oponente!')

            jogando = False

    lista_ataque_oponente = []

    linha_oponente = 0

    coluna_oponente = 0

    coordenada_oponente = [linha, coluna]
    
    while coordenada_oponente not in lista_ataque_oponente:
    
        linha_oponente = random.randint(0,9)

        coluna_oponente = random.randint(0,9)
        
        coordenada_oponente = [linha_oponente, coluna_oponente]

        if coordenada_oponente not in lista_ataque_oponente:

            tabuleiro_jogador = faz_jogada(tabuleiro_jogador, linha_oponente, coluna_oponente)

            lista_ataque_oponente.append(coordenada_oponente)
        
        navios_afundados_oponente = afundados(frota_jogador, tabuleiro_jogador)

        if navios_afundados_oponente == len(frota_jogador):

            print('Xi! O oponente derrubou toda a sua frota =(')

            jogando = False
