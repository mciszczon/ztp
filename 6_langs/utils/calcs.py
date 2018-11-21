from math import sqrt
from constants.calcs import COS, EUC


def cosinus_similiarity(phrase_dataset: dict, language_dataset: dict) -> float:
    """
    Returns a float between 0 and 1, where the lower result means more similiarity.
    """
    summed = 0
    len_phrase = 0
    len_language = 0

    for ngram in language_dataset.keys():
        summed += language_dataset[ngram] * (phrase_dataset.get(ngram) or 0)
        len_phrase += (phrase_dataset.get(ngram) or 0)**2
        len_language += language_dataset[ngram]**2

    return 1 - ( summed / ( sqrt(len_phrase) * sqrt(len_language) ) )


def euclides_similiarity(phrase_dataset: dict, language_dataset: dict) -> float:
    """
    TODO: What should it return?
    """
    summed = 0
    for ngram in language_dataset.keys():
        summed += (language_dataset[ngram] - (phrase_dataset.get(ngram) or 0))**2
    
    return sqrt(summed)


calc_functions = {
    COS: cosinus_similiarity,
    EUC: euclides_similiarity,
}