def is_valid(words: list) -> bool:
    if len(words) != 2:
        print("Podaj dokładnie dwa słowa!")
        return False

    if len(words[0]) != len(words[1]):
        print("Podaj słowa tej samej długości!")
        return False

    return True
\
def hamming_distance(str1: str, str2: str) -> int:
    counter = 0
    for x, y in zip(str1, str2):
        if x != y:
            counter += 1

    return counter


def main() -> bool:
    print("Enter two words of the same length.")
    phrase = input()
    words = phrase.split()

    if not is_valid(words):
        return False

    print(hamming_distance(*words))

    return True


if __name__ == "__main__":
    main()