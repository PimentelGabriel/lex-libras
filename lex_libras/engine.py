import spacy
from spacy.tokens import Doc, Token
# from spacy.tokens import 

# Meta dados sobre a frase
Doc.set_extension("tipo_frase", default=0)
'''
Esse metadado dirá como dese ser realizado a organização da sintax
Como por exemplo se uma frase não tiver sujeit explicito?
E por ai vai

DEVE SER MELHOR IMPLEMENTADO
'''

# Meta dado de todos os token para dizer que a palavra é traduzida e usada na glosa Libras
Token.set_extension("eh_corresponde", default=False)

# Meta dados da palavra, como por exemplo a forma em glosa
# Ex.:  PT-br               Glosa LIBRAS
#       ELES DERAM PRA ELA  EL@S 3pDAR3s EL@
#
Token.set_extension("metaDados", default={
    "palavra": None,
    "claseGramatical": None,
    "ordem": None
    }
)

nlp = spacy.load("pt_core_news_lg")

from .functions.core_translater import CoreTranslater
from .functions.graph_morph_changer import GraphMorphChanger

# from .functions.sintatic_organizer import sintaticOrganizer

import vlibras_translate
vlibras_tradutor = vlibras_translate.translation.Translation()

# for token in doc:
#     print(token.text, token.lemma_.upper(), token.pos_, token.dep_)

class TradutorLexLibras:
    glosaVlibras = ""
    docSpaCy = ""
    glosa = ""

    def traduzir(self, text):
        #self.glosaVlibras = vlibras_tradutor.rule_translation(text)
        self.docSpaCy = nlp(text)

        self.__core_translater()
        # self.__printMetaData()

        self.__graph_morph_changer()
        # self.__printMetaData()

        
        self.__sintatic_organizer()
        self.__printMetaData()

    def __core_translater(self):
        print("__core_translater is in implementation state")
        with CoreTranslater() as coreTranslater:
            coreTranslater.analisar(self.docSpaCy) 

    def __graph_morph_changer(self):
        print("__graph_morph_changer not implemented yet")
        # graphMorphChanger = GraphMorphChanger()
        with GraphMorphChanger() as graphMorphChanger: 
            graphMorphChanger.analisar(self.docSpaCy)

    def __sintatic_organizer(self):
        print("__sintatic_organizer not implemented yet")

    def __printMetaData(self):
        selected = []
        for token in self.docSpaCy:
            if token._.eh_corresponde:
                selected.append(token._.metaDados['palavra'])

        print(selected)
        

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
