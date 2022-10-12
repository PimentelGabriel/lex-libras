import spacy
from spacy.tokens import Token

from functions.core_translater import coreTranslater
from functions.graph_morph_changer import graphMorphChanger
from functions.sintatic_organizer import sintaticOrganizer


nlp = spacy.load("pt_core_news_lg")
doc = nlp("Vamos combater o mosquito da dengue!")

# for token in doc:
#     print(token.text, token.lemma_.upper(), token.pos_, token.dep_)


def glosaTest(token):
    if token.pos_ == "VERB":
        return "1p"+token.text+"2s"
    else:
        return token.text+"--testado"


Token.set_extension(name="wGlosa", getter=glosaTest,  force=True)

for token in doc:
    print(token.text)


for token in doc:
    print(token._.wGlosa)
