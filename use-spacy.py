import numpy as np
from array import array
import spacy
from spacy.lang.pt.examples import sentences

nlp = spacy.load("pt_core_news_sm")
doc = nlp("Vamos combater a dengue!")
# print(doc.text)

doc[0].set_morph("Mood=Imp|VerbForm=Fin")
assert "Mood=Imp" in doc[0].morph
assert doc[0].morph.get("Mood") == ["Imp"]
print(doc[0].morph.get("Mood"))

# print(frase[0])

# rint(frase)

# for token in doc:
#     print(token.text, token.lemma_, token.pos_, token.dep_)


# spacy.displacy.serve(doc, style="dep")

# nlp = spacy.load("en_core_web_sm")
# doc = nlp("displaCy uses JavaScript, SVG and CSS.")
