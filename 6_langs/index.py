import os
from utils.handler import Handler
from utils.ngram import Ngram
from utils.helpers import words_from_line, create_datasets
from utils.calcs import cosinus_similiarity
from constants.languages import TEST_LANGS, LANGUAGES, POL, ENG, GER, ITA, SPA, FIN

"""
Main Block
"""

def main():
    print("Language guesser. Enter a phrase consisting of at least few words:")
    phrase = input()
    phrase_ngram = Ngram(words_from_line(phrase))

    phrase_dataset = phrase_ngram.get_dataset()
    languages_datasets = create_datasets(LANGUAGES, Handler, Ngram)
    languages_similiarity = dict()

    for language in LANGUAGES:
        languages_similiarity[language] = cosinus_similiarity(phrase_dataset, languages_datasets[language])

    print(languages_similiarity)
        
    return True

if __name__ == "__main__":
  main()