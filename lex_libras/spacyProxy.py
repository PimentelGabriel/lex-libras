import spacy
from spacy.matcher import Matcher

nlp = spacy.load("pt_core_news_lg")

matcher = Matcher(nlp.vocab)

# Match para pegar substantivos compostos
subsComp = [
    {"POS": "NOUN", "DEP": "obj"},
    {"POS": "ADP", "DEP": "case", "OP": "?"},
    {"POS": "NOUN", "DEP": "nmod"}
]

matcher.add("subsComp", [subsComp])
