def analisarSubsPlur(token):
    if token.pos_ == "NOUN" and token.morph.get("Number")[0] == "Plur":
        print("\t\tNOUN PLUR "+token.text)
        token._.metaDados["palavra"] = token._.metaDados["palavra"]+"++"
