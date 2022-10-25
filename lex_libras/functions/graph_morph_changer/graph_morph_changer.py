from .functions import *

class GraphMorphChanger:

    # @staticmethod
    def analisar(self, Doc):
        # Passa em cada token para analisar sua grafia e
        # assim fazer as alterações para Glosa LIBRAS
        for token in Doc:
        #     print(token.pos_)
            # Pronomes
            if token.pos_.startswith("PRON"):
                # print("Pronound fonud")
                if token.text.upper() in ('ELE', 'ELA'):
                    token._.metaDados["palavra"] = "EL@"
                elif token.text.upper() in ('ELES', 'ELAS'):
                    token._.metaDados["palavra"] = "EL@S"
                #else:
                    #token._.metaDados["palavra"] = token.lemma_.upper()
            # Verbos
            elif token.pos_.startswith("VERB"):
                analisarVerbo(token, Doc)

            # Auxiliar
            elif token.pos_.startswith("AUX"):
                token._.metaDados["palavra"] = token.lemma_.upper()

            # Adjetivos
            # Para analisar os adjetivos devemos capturar os pronomes do qual o mesmo se refere
            elif token.pos_ == "NOUN" or token.pos_ == "PROPN" or token.pos_ == "PRON":
                analisarAdjetivo(token, Doc)
                # Add o ++ para cada substantivo no plural
                analisarSubsPlur(token)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        None
        # print("Tchau")