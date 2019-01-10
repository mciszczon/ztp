from utils.handler import Handler


def main() -> None:
    handler = Handler("sjp/odm.txt", "sjp/words.txt")
    handler.save()

    print("Zapisano słowa posortowane a tergo do pliku sjp/words.txt")


if __name__ == "__main__":
    main()
