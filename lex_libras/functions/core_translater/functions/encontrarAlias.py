from lex_libras.dto.palavraCandidataDTO import palavraCandidataDTO
from lex_libras.functions.utils.services.fetch_conjugation_verb import fetchInfinitiveForm


def encontrarAlias(Doc) -> None:
    for token in Doc:
        print(
            f"\t\t[NOTICE]: Fething: {token.text}\n\t\t\ttoken._.eh_corresponde: {token._.eh_corresponde}")
        if token._.eh_corresponde:
            if token.pos_ == 'VERB':
                print(token.pos_)
                checked = False
                # Procura o a caracteristica especifica para ver se a palavra é selecionável

                # Ver se a palavra é um pronome
                for c in token.children:
                    if c.pos_ == "PRON" and c.dep_ == "nsubj":
                        print("In for")
                        checked = True
                        break
                print("Next out for")

                if checked:
                    checked = False
                    if token.morph.get("VerbForm")[0] == "Fin" and token.morph.get("Mood")[0] == "Sub":
                        print(f"\t\t[NOTICE]: Fething: {token.text}")
                        palavra = fetchInfinitiveForm(token.text)

                        Doc._.candidateWords.addNewCandidateWord(
                            palavraCandidataDTO(
                                token.i,
                                palavra,
                                2
                            )
                        )

                    return None

                print(token.morph)

                if token.morph.get('Tense'):
                    if token.morph.get('Tense')[0] == "Past":
                        print(token.morph.get('Tense'))
                        palavra = fetchInfinitiveForm(token.text)
                        Doc._.candidateWords.addNewCandidateWord(
                            palavraCandidataDTO(
                                token.i,
                                palavra,
                                2
                            )
                        )

                    return None

                return None
