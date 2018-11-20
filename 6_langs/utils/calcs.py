from math import sqrt

def cosinus_similiarity(phrase_dataset: dict, language_dataset: dict) -> float:
    summed = 0
    len_phrase = 0
    len_language = 0

    for ngram in language_dataset.keys():
        summed += language_dataset[ngram] * (phrase_dataset.get(ngram) or 0)
        len_phrase += (phrase_dataset.get(ngram) or 0)**2
        len_language += language_dataset[ngram]**2

    return 1 - ( summed / ( sqrt(len_phrase) * sqrt(len_language) ) )