import os
from spacy.tokens import Token

# Essa função deve remover os sujeitos nominais de uma frase PT-br para não ser usada em uma frase LIBRAS


def removeNSubj(token: Token) -> None:
    # Procura conjunções para ser marcada como unutilisavel na glasa <token>._.eh_corresponde: Boolean
    # Só aciona palavras cuja as classes exite em LIBRAS
    if token.pos_.upper() == "VERB":
        for c in token.children:
            if c.dep_ == "nsubj":
                c._.eh_corresponde = False

        if os.environ['LEXLIBRAS_VERBOSE'] == "1":
            print(
                f"Particula {token.text} não elegível.\n\t\tA particula é um nsubj do verbo {token.text}")

    # print("removeConj in implementing state")
