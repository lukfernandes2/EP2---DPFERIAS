def define_posicoes(dados_de_posicionamento):
    retorno = []
    for i in range(dados_de_posicionamento["tamanho"]):
        if dados_de_posicionamento["orientacao"] == "vertical":
            retorno.append([i+dados_de_posicionamento["linha"], dados_de_posicionamento["coluna"]])
        elif dados_de_posicionamento["orientacao"] == "horizontal":
            retorno.append([dados_de_posicionamento["linha"], i+dados_de_posicionamento["coluna"]])
    return retorno
