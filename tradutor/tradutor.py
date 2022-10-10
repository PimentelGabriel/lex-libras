import spacy

from functions.core_translater import coreTranslater
from functions.graph_morph_changer import graphMorphChanger
from functions.sintatic_organizer import sintaticOrganizer


nlp = spacy.load("pt_core_news_lg")
doc = nlp("Vamos combater o mosquito da dengue!")

for token in doc:
    print(token.text, token.lemma_.upper(), token.pos_, token.dep_)
