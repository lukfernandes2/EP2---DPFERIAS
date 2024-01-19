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