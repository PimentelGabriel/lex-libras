# Essa função deve remover os artigos de uma frase PT-br para não ser usada em uma frase LIBRAS

def removeArt(token):
    if token.pos_ == 'DET':
        if token.morph.get('PronType')[0] == 'Art':
            token._.eh_corresponde = False

    # print("removeArt in implementing state")