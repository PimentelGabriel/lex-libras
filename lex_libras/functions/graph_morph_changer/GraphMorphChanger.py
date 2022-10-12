class GraphMorphChanger:
    def analisar(doc):
        # Passa em cada token para analisar sua grafia e
        # assim fazer as alterações para GLosa LIBRAS
        for token in doc:
            # Pronomes
            if token.dep_.startswith("PRO"):
                if token.upper in ('ELE', 'ELA'):
                    token._.metaDados["palavra"] = "EL@"
                elif token.upper in ('ELES', 'ELAS'):
                    token._.metaDados["palavra"] = "EL@S"
                else:
                    token._.metaDados["palavra"] = token.text.upper
            # Verbos
            if token.dep_.startswith("VERB"):
                token._.metaDados["clasePalavra"] = token.dep_
