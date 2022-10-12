import spacy
from spacy.tokens import Token

nlp = spacy.load("pt_core_news_lg")

# from functions.core_translater import coreTranslater
# from functions.graph_morph_changer import graphMorphChanger
# from functions.sintatic_organizer import sintaticOrganizer

import vlibras_translate
vlibras_tradutor = vlibras_translate.translation.Translation()

# for token in doc:
#     print(token.text, token.lemma_.upper(), token.pos_, token.dep_)

class TradutorLexLibras:
    glosaVlibras = ""
    docSpaCy = ""
    glosa = ""

    def traduzir(self, text):
        self.glosaVlibras = vlibras_tradutor.rule_translation(text)
        self.docSpaCy = nlp(text)

    def __graph_morph_changer(self):
        

    # def __init__(self):
        # return self

    def __enter__(self):
        return self

    # def __exit__(self, exc_type, exc_val, exc_tb):
    #     self.session.close()













# def glosaTest(token):
#     if token.pos_ == "VERB":
#         return "1p"+token.text+"2s"
#     else:
#         return token.text+"--testado"


# Token.set_extension(name="wGlosa", getter=glosaTest,  force=True)

# for token in doc:
#     print(token.text)


# for token in doc:
#     print(token._.wGlosa)
