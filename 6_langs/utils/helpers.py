import re

def words_from_line(line: str) -> list:
    "Zwraca listę słów dla linijki tekstu unicode."
    words = re.split(r'[\W\d]+', line)
    return [w.lower() for w in words if w]