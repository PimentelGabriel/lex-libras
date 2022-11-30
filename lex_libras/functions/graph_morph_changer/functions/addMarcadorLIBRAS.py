import os


def addMarcadorLIBRAS(doc):
    for token in doc:
        # Capturando a palavra que encadeia as outras de uma sequencia

        if token.pos_ == "NOUN":
            if token.dep_ == "nmod":
                print(f"\naddMarcadorLIBRAS: {token.text}\n")
                sumChildren = 0
                # Marca os tokens que devem receber os marcadores
                for i in token.children:
                    sumChildren += 1

                if sumChildren > 2:
                    doc._.possuiMarcador = True
                    token._.metaDados["possuiMarcadorLIBRAS"] = True
                    token._.metaDados["ehLinkavel"] = False
                else:
                    print("Não precisa de marcador LIBRAS")
                    continue

                # numMarc = 0
                # for tokenC in token.children:
                #     numMarc += 1
                    # if tokenC.pos_ == "ADJ":

                # Filhos de primerio grau, que fazem parte da lista
                for tokenC in token.children:
                    if tokenC.pos_ == "NOUN":
                        if tokenC.dep_ == "conj":
                            # Filhos de seungo grau, que dependem da palavra que faz parte da lista
                            if tokenC.children:  # Se essa palavra possui outras palavras que dependem dela
                                # Remove o marcador libras pois se trata de uma palavra
                                tokenC._.metaDados["possuiMarcadorLIBRAS"] = False

                                # addInChild = True
                                idChildInDoc = -1
                                for subChild in tokenC.children:
                                    if subChild.pos_ == "ADJ" and subChild.dep_ == "amod":
                                        idChildInDoc = subChild.i

                                # Se nenhum dos seus filhos forem elegivel para receber o marcador
                                if idChildInDoc == -1:
                                    # è devolvido o marcador para o filho de primeiro grau
                                    tokenC._.metaDados["possuiMarcadorLIBRAS"] = True
                                    tokenC._.metaDados["ehLinkavel"] = False
                                else:
                                    doc[idChildInDoc]._.metaDados["possuiMarcadorLIBRAS"] = True
                                    doc[idChildInDoc]._.metaDados["ehLinkavel"] = False

                            else:  # if you have a token that don't have a child
                                tokenC._.metaDados["possuiMarcadorLIBRAS"] = True
                                tokenC._.metaDados["ehLinkavel"] = False

                # Adicionando o marcador libras nos tokens anteriomente mapeados

    numMarc = 1
    for token in doc:
        print(token.text)
        if token._.metaDados['possuiMarcadorLIBRAS']:
            print(f"#{token.text}")
            token._.metaDados["palavra"] = f"{token._.metaDados['palavra']} MARCADOR-{numMarc}"
            numMarc += 1
