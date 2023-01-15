import os
from spacy.tokens import Token


def getPronouns(token: Token) -> str:
    try:
        pron = {
            "Sing": {
                "1": "EU",
                "2": "VOCÊ",
                "3": {
                    "female": "ELA",
                    "male": "ELE",
                    "nether": "EL@"
                }
            },
            "Plur": {
                "1": "NÓS",
                "2": "VOCÊS",
                "3": {
                    "female": "ELAS",
                    "male": "ELES",
                    "nether": "EL@S"
                }
            }
        }

        if token.morph.get('VerbForm') == "Fin":
            if token.morph.get('Number')[0] == "Plur":
                if token.morph.get('Person')[0] == "3":
                    return pron["Plur"]["3"]["nether"]

                elif token.morph.get('Person')[0] in ["1", "2"]:
                    print("Precisa-se implementar quando usar o netro ou não")
                    return pron["Plur"][token.morph.get('Person')[0]]
                else:
                    raise Exception(
                        f"Na análise morpológica da palvra não foi encontrado o atributo 'Person'.\n\tO atributo diz respeito ao pessoa do discurso")

            elif token.morph.get('Number')[0] == "Sing":
                if token.morph.get('Person')[0] == "3":
                    return pron["Sing"]["3"]["nether"]

                elif token.morph.get('Person')[0] in ["1", "2"]:
                    print("Precisa-se implementar quando usar o neutro ou não")
                    return pron["Sing"][token.morph.get('Person')[0]]
                else:
                    raise Exception(
                        f"Na análise morpológica da palvra não foi encontrado o atributo 'Person'.\n\tO atributo diz respeito ao pessoa do discurso")
            else:
                raise Exception(
                    f"Na análise morpológica da palvra não foi encontrado o atributo 'Number'")

    except Exception as e:
        print(f"Erro na palavra '{token.text}'\n\t{e}")
