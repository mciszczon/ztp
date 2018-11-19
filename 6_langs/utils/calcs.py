from math import sqrt

def cosinus_similiarity(phrase_dataset: dict, language_dataset: dict) -> float:
    """
    TODO: Refactor
    TODO: Check formula (it returns negative numbers now)
    """
    summed = 0
    len_phrase = 0
    len_language = 0

    for ngram in phrase_dataset.keys():
        summed += phrase_dataset[ngram] * (language_dataset.get(ngram) or 0)
        len_phrase += phrase_dataset[ngram]^2

    for ngram in language_dataset.keys():
        len_language += language_dataset[ngram]^2

    return 1 - ( summed / ( sqrt(len_phrase) * sqrt(len_language) ) )