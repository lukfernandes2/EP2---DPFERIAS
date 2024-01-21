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