import os
from utils.handler import Handler
from utils.ngram import Ngram
from utils.helpers import words_from_line
from constants.languages import TEST_LANGS, LANGUAGES, POL, ENG, GER, ITA, SPA, FIN

"""
1. Tworzę 1-, 2-, 3-gramy (może być więcej) dla obu porównywanych języków (tekstów). W ten sposób powstaje `x` i `y`.
   Porównuję tylko ngramy o takiej samej krotności! Czyli 1-gramy `x` z 1-gramami `y` itd.
   Są one częścią tego samego wektora, np. { 'a': 312, ..., 'ab': 12, ... }
2. x1 i y1 to odpowiadające sobie ngramy, np. 'al' i 'al' – a dokładniej ich wartości (częstością występowania).
3. Jeżeli dany ngram nie wystąpi w drugim tekście, to jego wartość powinna być przyjęta jako 0.

Długość wektora len(x): √x1^2 + x2^2 + x3^2 + ... + xn^2 (pierwiastek nad całością)
"""

"""
Main Block
"""

def main():
    print("Language guesser. Enter a phrase consisting of at least few words:")
    phrase = input()
    phrase_ngram = Ngram(words_from_line(phrase))
    phrase_dataset = phrase_ngram.get_dataset()

    languages_handlers = dict()
    language_datasets = dict()
    
    os.chdir(os.getcwd() + "/texts")
    for language in TEST_LANGS:
        handler = languages_handlers[language] = Handler(LANGUAGES[language])
        ngram = Ngram(handler.words)
        language_datasets[language] = ngram.get_dataset()

    import pdb; pdb.set_trace()
        
    return True

if __name__ == "__main__":
  main()