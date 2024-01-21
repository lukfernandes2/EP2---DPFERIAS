import random

# PARA TESTAS O SEU CÓDIGO NA ACADEMIA PYTHON SERÁ NECESSÁRIO COLAR AS FUNÇÕES DESENVOLVIDAS AQUI!!!

def define_posicoes(dados_de_posicionamento):
    retorno = []
    for i in range(dados_de_posicionamento["tamanho"]):
        if dados_de_posicionamento["orientacao"] == "vertical":
            retorno.append([i+dados_de_posicionamento["linha"], dados_de_posicionamento["coluna"]])
        elif dados_de_posicionamento["orientacao"] == "horizontal":
            retorno.append([dados_de_posicionamento["linha"], i+dados_de_posicionamento["coluna"]])
    return retorno

def preenche_frota (dados_de_posicionamento, nome_navio, frota):

    dados_de_posicionamento = define_posicoes(dados_de_posicionamento)

    nova_embarcacao = {}

    nova_embarcacao["tipo"] = nome_navio

    nova_embarcacao["posicoes"] = dados_de_posicionamento

    frota.append(nova_embarcacao)

    return frota

def faz_jogada(tabuleiro,linha,coluna):
    if tabuleiro[linha][coluna] == 1:
        tabuleiro[linha][coluna] = "X"
    elif tabuleiro[linha][coluna] == 0:
        tabuleiro[linha][coluna] = "-"
    return tabuleiro

def posiciona_frota (frota):

    tabuleiro_atualizado = [
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
  ]

    for embarcacao in frota:

        for posicao, numeros in embarcacao.items():

            if posicao == "posicoes":

                coordenadas = embarcacao[posicao]
        
                for i in range(len(tabuleiro_atualizado)):

                    for coordenada in coordenadas:

                        if coordenada[0] == i:

                            for j in range(len(tabuleiro_atualizado[i])):
                                if j == coordenada[1]:

                                    tabuleiro_atualizado[i][j] = 1
    
    return tabuleiro_atualizado

def afundados(frota, tabuleiro):
    afundados = 0
    for embarcacao in frota:
        cont_X = 0
        for loc in embarcacao["posicoes"]:
            if tabuleiro[loc[0]][loc[1]] == "X":
                cont_X += 1
        if cont_X == len(embarcacao["posicoes"]):
            afundados += 1
    return afundados

def posicao_valida(dados_de_posicionamento, frota):
    posicao = define_posicoes(dados_de_posicionamento)
    for elem in posicao:
        if elem[0] > 9 or elem[1] > 9:
            return False
    for embarcacao in frota:
        for loc in embarcacao["posicoes"]:
            if loc in posicao:
                return False
                
    return True



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
    
        linha = input(int("Qual linha você deseja atacar?"))

        while linha < 0 or linha > 9:

            print("Linha inválida!")

            linha = input(int("Qual linha você deseja atacar?"))

        coluna = input(int("Qual coluna você deseja atacar?"))

        while coluna < 0 or coluna > 9:

            print("Linha inválida!")

            coluna = input(int("Qual coluna você deseja atacar?"))

            
        
    




    # TODO: Implemente aqui a lógica para verificar se a linha e coluna não foram escolhidas anteriormente
    # TODO: Implemente aqui a lógica para verificar se o jogador derrubou todos os navios do oponente
