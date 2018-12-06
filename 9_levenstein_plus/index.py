from utils.levenstein import Levenstein


def main() -> None:
    pairs = [
        ('pies', 'pies'),
        ('granat', 'granit'),
        ('orczyk', 'oracz'),
        ('marka', 'ariada'),
        ('izrael', 'stein'),
        ('izrael', 'blumensztajn'),
    ]

    for pair in pairs:
        print(Levenstein(*pair))


if __name__ == "__main__":
    main()