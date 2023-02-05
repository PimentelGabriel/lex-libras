import os
from lex_libras.functions.utils.get_pronouns import getPronouns
from lex_libras.functions.utils.services.fetch_conjugation_verb import fetchInfinitiveForm


def analisarVerbo(token, Doc):
    if os.environ['LEXLIBRAS_VERBOSE'] == "1":
        print(f"Dentro de {__file__}")
        print(f"analisarVerbo({token.text}:str)")

    token._.metaDados["verboData"] = {
        "numero": '*',
        "pessoa": "*",
        "obj": {
            "numero": "*",
            "pessoa": "*"
        }
    }

    # token._.metaDados["claseGramatical"]

    # Analisa se o verbo não está no presente
    # caso positivo ele passará para o infinitivo
    # Caso a frase termine com '!' (excalmação) ele colocará a particula 'JÁ'
    if token.morph.get('Tense'):
        if token.morph.get('Tense') == "Past" and token.doc[len(token.doc)-1].text == "!":
            token._.metaDados['ehLinkavel'] = False
            token._.metaDados['palavra'] = fetchInfinitiveForm(
                token.lemma_) + " JÁ"

    # Obter flag do banco de dados para tratar adequadamente cada verbo
    if token._.metaDados["claseGramatical"] == 'VERB-P':
        if os.environ['LEXLIBRAS_VERBOSE'] == "1":
            print("Pêgo o verbo "+token.text)

        if token.dep_ == "ROOT":
            # Obtem o numero (singular ou plural) e a pessoa (1º, 2º ou 3º) do sujeito da frase pra concatenar com o verbo principal
            if token.morph.get('Person'):
                if token.morph.get('Number')[0] == "Sing":
                    token._.metaDados["verboData"]["numero"] = 's'    
                else:
                    token._.metaDados["verboData"]["numero"] = 'p'

                token._.metaDados["verboData"]["pessoa"] = token.morph.get('Person')[0]

            else:
                for c in token.children:
                    # Analisa o auxiliar para ver se é um verbo e se for deve
                    # conter informações sobre o tempó e a pessoa do discuro
                    if c.pos_ == "AUX" and c.morph.get('VerbForm'):
                        if c.morph.get('Number')[0] == "Sing":
                            token._.metaDados["verboData"]["numero"] = 's'
                        else:
                            token._.metaDados["verboData"]["numero"] = 'p'

                        token._.metaDados["verboData"]["pessoa"] = c.morph.get('Person')[0]

            # Analisa os outros auxilires do verbo principal
            for c in token.children:
                # Caso o fihlo seja um sujeito
                if c.dep_ == "nsubj":
                    if c.pos_.startswith("PRON"):
                        #Como um token sintaqticamente filho do verbo conjugado pela pessoa discurso (verbo-p) é um pronome
                        # O algoritimo deve invalidar o PRON
                        c._.eh_corresponde = False

                # Caso o filho seja um objeto ou obliquo
                if c.dep_ in ("obj", "obl"):
                    if os.environ['LEXLIBRAS_VERBOSE'] == "1":
                        print("\n\n\t\tVERBOSE!!!!!!!!\n\n")
                        print(f"{c.text} é {c.dep_} e o seu pos é {c.pos_}")
                        print("Veja o morph")
                        print(c.morph)

                    # Ver se é substantivo
                    if c.pos_.startswith("NOUN"):
                        if c.morph.get('Number')[0] == "Sing":
                            token._.metaDados["verboData"]["obj"]["numero"] = 's'
                        elif c.morph.get('Number')[0] == 'p':
                            token._.metaDados["verboData"]["obj"]["pessoa"] = '3'

                        if c.morph.get('Number')[0] not in ("Sing", "Plur"):
                            raise Exception(
                                f"Número da palavra {c.text} não encontrada.\n\tA palavra deve ser um objeto, porém não possui\nNumber")
                        break
                    
                    # Ver se é pronome
                    # Verificar essa regras
                    if c.pos_.startswith("PRON"):
                        #Como um token sintaqticamente filho do verbo conjugado pela pessoa discurso (verbo-p) é um pronome
                        # O algoritimo deve invalidar o PRON
                        c._.eh_corresponde = False

                        if c.morph.get('Number')[0] == "Sing":
                            token._.metaDados["verboData"]["obj"]["numero"] = 's'
                        else:
                            token._.metaDados["verboData"]["obj"]["numero"] = 'p'
                        
                        token._.metaDados["verboData"]["obj"]["pessoa"] = c.morph.get('Person')[0]
                        
                        if c.morph.get('Number')[0] not in ("Sing", "Plur"):
                            raise Exception(
                                f"Número da palavra {c.text} não encontrada.\n\tA palavra deve ser um objeto, porém não possui\nNumber")
                        break
                    
                    # Ver se é substantivo próprio
                    if c.pos_.startswith("PROPN"):
                        token._.metaDados["verboData"]["obj"]["numero"] = 's' if c.morph.get('Number')[
                            0] == "Sing" else 'p'
                        token._.metaDados["verboData"]["obj"]["pessoa"] = '3'
                        if c.morph.get('Number')[0] not in ("Sing", "Plur"):
                            raise Exception(
                                f"Número da palavra {c.text} não encontrada.\n\tA palavra deve ser um objeto, porém não possui\nNumber")
                        break

        palavraGlosa = token._.metaDados["verboData"]["pessoa"] +\
            token._.metaDados["verboData"]["numero"] +\
            token._.metaDados["palavra"] +\
            token._.metaDados["verboData"]["obj"]["pessoa"] +\
            token._.metaDados["verboData"]["obj"]["numero"]

        token._.metaDados["palavra"] = palavraGlosa

    if token._.metaDados["claseGramatical"] == 'VERB-G':
        raise Exception(
            'Tratativa para os verbos que são conjugado pelo gênero (VERB-G) não implementado')

    if token._.metaDados["claseGramatical"] == 'VERB-L':
        VERB_L_n_tratado = False
        for c in token.children:
            if c.pos_ in ("NOUN") and c.dep_ == "obj":
                VERB_L_n_tratado = True
                token._.metaDados["palavra"] = f"<{token._.metaDados['palavra']}-{c._.metaDados['palavra']}>"

        if not VERB_L_n_tratado and False:
            raise Exception(
                f"O verbo '{token.text.upper()}' conjugado por locativo.\n\tTratativa para os verbos que são conjugado pelo locativo (VERB-L) não implementado")

    if token._.metaDados["claseGramatical"] == 'VERB':
        pronoun = getPronouns(token)
        if pronoun:
            token._.metaDados["palavra"] = pronoun + \
                " "+token._.metaDados["palavra"]
        else:
            token._.metaDados["palavra"] = token._.metaDados["palavra"]
