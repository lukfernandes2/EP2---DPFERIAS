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


def posicao_valida (dados, frota): #PRECISA SER CORRIGIDA

    
    contador_falso = 0

    dados_de_posicao = define_posicoes(dados)

    for embarcacao in frota:

        for posicao, numero in embarcacao.items():

            if posicao == "posicoes":

                coordenadas = embarcacao[posicao]

                for coordenada in coordenadas:

                    for coordinate in dados_de_posicao:

                        if coordenada[0] == coordinate[0] and coordenada[1] == coordinate[1]:

                            contador_falso += 1
                        
                       
    

    if contador_falso > 0:

        return False
    
    else: 

        return True