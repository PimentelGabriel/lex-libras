import os

# Essa função deve remover as adposições* (preposições e pósposições)
# de uma frase PT-br para não ser usada em uma frase LIBRAS
# https://universaldependencies.org/u/pos/ADP.html

def removeAdp(token):
    if  token.pos_ == "ADP":
        # if token.text.upper() in ("A", "O", "AS", "OS", "DA", "DO", "DAS", "DOS"):

        token._.eh_corresponde = False

        if os.environ['LEXLIBRAS_VERBOSE'] == "1":
            print(f"Adiposição {token.text} não elegível")
    # print("removeArt in implementing state")