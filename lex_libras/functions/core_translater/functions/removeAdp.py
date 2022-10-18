# Essa função deve remover as adposições* de uma frase PT-br para não ser usada em uma frase LIBRAS
# https://universaldependencies.org/u/pos/ADP.html

def removeAdp(token):
    if  token.pos_ == "ADP":
        if token.text.upper() in ("A", "O", "AS", "OS"):
            token._.eh_corresponde = False

    # print("removeArt in implementing state")