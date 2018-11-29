from utils.levenstein import levenstein

"""
Macierz dwuwymiarowa, w jednym wymiarze słowo a, w drugim b.

Wynik z góry    +1
Wynik z lewej   +1
(-1, -1)        +1 lub +0 jeśli litery te same na przecięciu
"""

def main() -> bool:
    print(levenstein('pies', 'pies'))
    print(levenstein('granat', 'granit'))
    print(levenstein('orczyk', 'oracz'))
    print(levenstein('marka', 'ariada'))
    return True


if __name__ == "__main__":
    main()