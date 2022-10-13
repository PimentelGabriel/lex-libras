class GraphMorphChanger:

    # @staticmethod
    def analisar(self, Doc):
        # Passa em cada token para analisar sua grafia e
        # assim fazer as alterações para GLosa LIBRAS
        for token in Doc:
            print(token.pos_)
            # Pronomes
            if token.pos_.startswith("PRON"):
                print("Pronound fonud")
                if token.text.upper() in ('ELE', 'ELA'):
                    token._.metaDados["palavra"] = "EL@"
                elif token.text.upper() in ('ELES', 'ELAS'):
                    token._.metaDados["palavra"] = "EL@S"
                else:
                    token._.metaDados["palavra"] = token.text.upper()
            # Verbos
            elif token.pos_.startswith("VERB"):
                token._.metaDados["clasePalavra"] = token.dep_

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Tchau")