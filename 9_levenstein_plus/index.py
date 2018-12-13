from utils.levenstein import Levenstein


def main() -> None:
    pairs = [
        ('pierze', 'pieże'),  # 0.5
        ('smiech', 'śmiech'),  # 0.2
        ('piora', 'piórą'),  # 0.4
        ('piura', 'pióra'),  # 0.5
        ('człowiek', 'cłzoiwek'),  # 1.0
        ('zrobić', 'rzobić'),  # 0.5
        ('zrobzrić', 'rzobrzić'),  # 1.0
        ('zima', 'źima'),  # 0.2
        ('prosiłem', 'prsoilem'),  # 0.7
        ('ćwok', 'wciok'),  # 2.2
        ('izrael', 'zireal'),  # 0.5
    ]

    for pair in pairs:
        print(Levenstein(*pair))


if __name__ == "__main__":
    main()