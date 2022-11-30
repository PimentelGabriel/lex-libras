#import vlibras_translate
import os
import re
import spacy
from spacy.tokens import Doc, Token
from .functions.graph_morph_changer import GraphMorphChanger
from .functions.core_translater import CoreTranslater
from .functions.utils.split_keep_signal import splitKeepSignal

# from spacy.tokens import


# Setting if de execution is verbose
verbose = False

# Meta dados sobre a frase
Doc.set_extension("tipo_frase", default=0)
'''
Esse metadado dirá como dese ser realizado a organização da sintax
Como por exemplo se uma frase não tiver sujeit explicito?
E por ai vai

DEVE SER MELHOR IMPLEMENTADO
'''

# Meta dado para sinalizar que a frase possui marcadores
Doc.set_extension("possuiMarcador", default=False)

# Meta dado de todos os token para dizer que a palavra é traduzida e usada na glosa Libras
Token.set_extension("eh_corresponde", default=False)

# Meta dados da palavra, como por exemplo a forma em glosa
# Ex.:  PT-br               Glosa LIBRAS
#       ELES DERAM PRA ELA  EL@S 3pDAR3s EL@
#
Token.set_extension("metaDados", default={
    "palavra": None,
    # Atributo para dizer se o sistema deve substituir os espaços vazios por '-' ou não linkavel (ehLinkavel == True: o sistema substitui)
    "ehLinkavel": True,
    "claseGramatical": None,
    "ordem": None,
    "existeSinalLibras": False,
    "possuiMarcadorLIBRAS": False
}
)

nlp = spacy.load("pt_core_news_lg")


# from .functions.sintatic_organizer import sintaticOrganizer

#vlibras_tradutor = vlibras_translate.translation.Translation()

# for token in doc:
#     print(token.text, token.lemma_.upper(), token.pos_, token.dep_)

class TradutorLexLibras:
    __verbose = False
    glosaVlibras = ""
    docSpaCy = ""
    glosa = ""
    selected = ""

    def traduzir(self, text):
        #self.glosaVlibras = vlibras_tradutor.rule_translation(text)
        self.docSpaCy = nlp(text)

        self.__core_translater()
        # self.__printMetaData()

        self.__graph_morph_changer()
        # self.__printMetaData()

        self.__sintatic_organizer()
        self.__printMetaData()

        if os.environ['LEXLIBRAS_VERBOSE'] == "1":
            print(f"\n\tGLOSA:\t{self.__getGlosa()}\n")

        return self.__getGlosa()

    def __core_translater(self):
        print("__core_translater is in implementation state")
        with CoreTranslater() as coreTranslater:
            coreTranslater.analisar(self.docSpaCy)

    def __graph_morph_changer(self):
        print("__graph_morph_changer not completly implemented yet")
        # graphMorphChanger = GraphMorphChanger()
        with GraphMorphChanger() as graphMorphChanger:
            graphMorphChanger.analisar(self.docSpaCy)

    def __sintatic_organizer(self):
        print("__sintatic_organizer not implemented yet")

    def __getGlosa(self):
        glosa = ""
        firstPass = True
        for w in self.docSpaCy:
            if w._.eh_corresponde:
                if w._.metaDados["ehLinkavel"]:
                    w._.metaDados["palavra"] = re.sub(
                        "\s", "-", w._.metaDados["palavra"])
                if w.i == 0 or firstPass:
                    glosa = w._.metaDados["palavra"]
                    firstPass = False
                elif w.pos_ == 'PUNCT':
                    glosa += w._.metaDados["palavra"]
                else:
                    glosa += " " + w._.metaDados["palavra"]

        return glosa

    def __printMetaData(self):
        if self.__verbose:
            self.selected = []
            flags = []
            for token in self.docSpaCy:
                if token._.eh_corresponde:
                    self.selected.append(token._.metaDados['palavra'])
                    flags.append(token._.metaDados['existeSinalLibras'])

            print(self.selected)
            print(flags)

    def setVerboseMode(self, boolFlag):
        if isinstance(boolFlag, bool):
            self.__verbose = boolFlag
            os.environ['LEXLIBRAS_VERBOSE'] = "1" if boolFlag else "0"
            if boolFlag:
                print("\n\tVerbose mode activated!!!\n")
            else:
                print("\n\tVerbose mode disabled!!!\n")

        else:
            print("\n\n\tO parametro deve ser boleano!\n")

    def getVerboseMode(self):
        return self.__verbose

    # def __init__(self):
        # return self

    def __enter__(self):
        return self

    # def __exit__(self, exc_type, exc_val, exc_tb):
    #     self.session.close()


# tradutorLexLibras = TradutorLexLibras()


class Preparer():
    phrases = []
    glosas = []
    tradutorLexLibras = None

    def translate(self, intirePhrase):
        self.phrases = []
        self.glosas = []
        self.tradutorLexLibras = TradutorLexLibras()
        phrases = splitKeepSignal(intirePhrase)

        for phrase in phrases:
            self.glosas.append(self.tradutorLexLibras.traduzir(phrase))

        return self.getGlosasUnion()

    def getGlosasUnion(self):
        return ' '.join(self.glosas)

    def __enter__(self):
        self.tradutorLexLibras = TradutorLexLibras()
        return self

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
