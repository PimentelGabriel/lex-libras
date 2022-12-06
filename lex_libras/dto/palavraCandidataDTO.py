class palavraCandidataDTO:
    def __init__(self, idToken: int, palavra: str, peso: int) -> None:
        self.i = 0
        self.idToken = idToken
        self.palavra = palavra
        self.peso = peso
        self.elegido = 0
