from utils.matrix import Matrix


def main() -> None:
    print("Podaj pierwszy ciąg:")
    string1 = input()

    print("Podaj drugi ciąg:")
    string2 = input()

    matrix = Matrix(string1, string2)
    print(f"Najdłuższy wspólny podciąg: {matrix.right_bottom}")
    print(f"LCS: {matrix.lcs}")


if __name__ == "__main__":
    main()
