import re
import os

def words_from_line(line: str) -> list:
    "Zwraca listę słów dla linijki tekstu unicode."
    words = re.split(r'[\W\d]+', line)
    return [w.lower() for w in words if w]

def create_datasets(languages: dict, handler_class: 'Handler', ngram_class: 'Ngram') -> dict:
    language_datasets = dict()
    os.chdir(os.getcwd() + "/texts")
    for language in languages:
        handler = handler_class(languages[language])
        ngram = ngram_class(handler.words)
        language_datasets[language] = ngram.get_dataset()

    return language_datasets