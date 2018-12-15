from .text_handler import TextHandler


class Converter:

    def __init__(self, text_handler: TextHandler, rules: dict) -> None:
        self.text_handler = text_handler
        self.rules = rules

    @property
    def transposed(self):
        return " ".join(self._convert())

    def _convert(self):
        result = []
        for word in self.text_handler.words:
            result.append(self._transpose(word))

        return result

    def _transpose(self, word):
        array = list(word.lower())
        size = len(word)

        converted = []

        for letter in array:
            rule = self.rules.get(letter)
            if not rule:
                converted.append(letter)
            else:
                converted.append(rule)

        return "".join(converted)