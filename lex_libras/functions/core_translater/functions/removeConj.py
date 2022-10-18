# Essa função deve remover as conjunções de uma frase PT-br para não ser usada em uma frase LIBRAS

def removeConj(token):
    # Procura conjunções para ser marcada como unutilisavel na glasa <token>._.eh_corresponde: Boolean
    # Só aciona palavras cuja as classes exite em LIBRAS
    if token.pos_.upper() not in (
        "CCONJ", # Conjunção coordenativa
        "SCONJ", # Conjunção subordinada
    ):
        token._.eh_corresponde = True

    
    # print("removeConj in implementing state")