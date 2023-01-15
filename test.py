import spacy
from spacy.matcher import Matcher

nlp = spacy.load("pt_core_news_lg")

matcher = Matcher(nlp.vocab)

f3 = nlp("Por isso temos que manter a caixa de água fechada! Vamos embora usando um bico de pato como brinqueno de estimação.")

# Match para pegar substantivos compostos
subsComp = [
    {"POS": "NOUN", "DEP": "obj"},
    {"POS": "ADP", "DEP": "case", "OP": "?"},
    {"POS": "NOUN", "DEP": "nmod"}
]

getVerb = [
    {"POS": "VERB"}
]

matcher.add("getVerb", [getVerb])
matcher.add("subsComp", [subsComp])

captura = matcher(f3)
