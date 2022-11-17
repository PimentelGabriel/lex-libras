def aglutinarPalavra(Doc):
    for token in Doc:

        # Aglutina Pronomes e preposições
        if token.pos_ in ("PRON"):
            if token.morph.get("PronType")[0] in ("Dem"):
                for child in token.children:
                    if child.pos_ in ("ADP"):
                        token._.metaDados["palavra"] = child.text.upper() + " " + token.text.upper()
                        if os.environ['LEXLIBRAS_VERBOSE'] == "1":
                            print(f"Palavra aglutinada: {token._.metaDados['palavra']}");