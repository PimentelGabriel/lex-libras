def analisarVerbo(token, Doc):
    print("\n\tHELLO")
    token._.metaDados["verboData"] = {
        "numero": '*',
        "pessoa": "*",
        "obj": {
            "numero": "*",
            "pessoa": "*"
        }
    }
    
    # token._.metaDados["claseGramatical"]
    
    
    # Obter flag do banco de dados para tratar adequadamente cada verbo
    if token._.metaDados["claseGramatical"] == 'VERB-P':
        print("Pêgo o verbo "+token.text)

        if token.dep_ == "ROOT":
            # Obtem o numero (singular ou plural) e a pessoa (1º, 2º ou 3º) do sujeito da frase pra concatenar com o verbo principal
            if token.morph.get('Person'):
                token._.metaDados["verboData"]["numero"] = 's' if token.morph.get('Number')[0] == "Sing" else 'p' 
                token._.metaDados["verboData"]["pessoa"] = token.morph.get('Person')[0] 

            else:
                for c in token.children:
                    # Analisa o auxiliar para ver se é um verbo e se for deve
                    # conter informações sobre o tempó e a pessoa do discuro
                    if c.pos_ == "AUX" and c.morph.get('VerbForm'):
                        token._.metaDados["verboData"]["numero"] = 's' if c.morph.get('Number')[0] == "Sing" else 'p'
                        token._.metaDados["verboData"]["pessoa"] = c.morph.get('Person')[0]
            
            # Analisa os outros auxilires do verbo principal
            for c in token.children:
                    # Caso seja o objeto
                    if c.dep_ == "obj":
                        print(f"{c.text} é {c.dep_} e o seu pos é {c.pos_}")
                        print("Veja o morph")
                        print(c.morph)
                        # Ver se é substantivo
                        if c.pos_.startswith("NOUN"):

                            token._.metaDados["verboData"]["obj"]["numero"] = 's' if c.morph.get('Number')[0] == "Sing" else 'p'
                            token._.metaDados["verboData"]["obj"]["pessoa"] = '3'
                            if c.morph.get('Number')[0] not in ("Sing", "Plur"):
                                raise Exception(f"Número da palavra {c.text} não encontrada.\n\tA palavra deve ser um objeto, porém não possui\nNumber")
                            break
                        # Ver se é pronome 
                        # Verificar essa regras
                        if c.pos_.startswith("PRON"): 
                            token._.metaDados["verboData"]["obj"]["numero"] = 's' if c.morph.get('Number')[0] == "Sing" else 'p'
                            token._.metaDados["verboData"]["obj"]["pessoa"] = c.morph.get('Person')[0]
                            if c.morph.get('Number')[0] not in ("Sing", "Plur"):
                                raise Exception(f"Número da palavra {c.text} não encontrada.\n\tA palavra deve ser um objeto, porém não possui\nNumber")
                            break
                        # Ver se é substantivo próprio
                        if c.pos_.startswith("PROPN"): 
                            token._.metaDados["verboData"]["obj"]["numero"] = 's' if c.morph.get('Number')[0] == "Sing" else 'p'
                            token._.metaDados["verboData"]["obj"]["pessoa"] = '3'
                            if c.morph.get('Number')[0] not in ("Sing", "Plur"):
                                raise Exception(f"Número da palavra {c.text} não encontrada.\n\tA palavra deve ser um objeto, porém não possui\nNumber")
                            break
    palavraGlosa =  token._.metaDados["verboData"]["pessoa"]+token._.metaDados["verboData"]["numero"]+token._.metaDados["palavra"]+token._.metaDados["verboData"]["obj"]["pessoa"]+token._.metaDados["verboData"]["obj"]["numero"]

    token._.metaDados["palavra"] = palavraGlosa