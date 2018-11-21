import os
from utils.handler import Handler
from utils.ngram import Ngram
from utils.helpers import words_from_line, create_datasets
from utils.calcs import calc_functions
from constants.languages import TEST_LANGS, LANGUAGES
from constants.calcs import COS, EUC, CALCS

"""
Main Block
"""

def main():
    print("Language guesser. Enter a phrase consisting of at least few words:")
    phrase = input()
    phrase_ngram = Ngram(words_from_line(phrase))

    print("Which calculus to use? 1 – {}; 2 — {}".format(COS, EUC))
    calc_function = input()

    try:
        calc_function = int(calc_function)
        if calc_function != 1 and calc_function != 2:
            raise Exception
    except Exception:
        print("You supplied invalid argument. Falling back to {} calculus function.".format(COS))
        calc_function = 1


    phrase_dataset = phrase_ngram.get_dataset()
    languages_datasets = create_datasets(LANGUAGES, Handler, Ngram)
    function_loader = CALCS[calc_function-1]
    languages_similiarity = dict()

    for language in LANGUAGES:
        languages_similiarity[language] = calc_functions[function_loader](phrase_dataset, languages_datasets[language])

    print(languages_similiarity)
        
    return True

if __name__ == "__main__":
  main()