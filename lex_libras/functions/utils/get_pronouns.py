def getPronouns(token):

    pronounes = {
        "Sing":
            "1": "EU",
            "2": "VOCÊ",
            "3":
                "female": "ELA",
                "male": "ELE",
                "nether": "EL@",
        "Plur":
            "1": "NÓS",
            "2": "VOCÊS",
            "3":
                "female": "ELAS",
                "male": "ELES",
                "nether": "EL@S"
    }

    if token.morphObject.get('Number')[0] == "Plur":
        if token.morphObject.get('Person')[0] == "3":
            return pronounes["Plur"]["3"]["nether"]
            
        elif orphObject.get('Person')[0] in ["1", "2"]:
            print("Precisa-se implementar quando usar o netro ou não")
            return pronounes["Plur"][orphObject.get('Person')[0]]

    elif token.morphObject.get('Number')[0] == "Sing":
        if token.morphObject.get('Person')[0] == "3":
            return pronounes["Sing"]["3"]["nether"]
            
        elif token.morphObject.get('Person')[0] in ["1", "2"]:
            print("Precisa-se implementar quando usar o neutro ou não")
            return pronounes["Sing"][orphObject.get('Person')[0]]
    else:
        raise Exception(f"Na análise morpológica da palvra não foi encontrado o atributo 'Number'")