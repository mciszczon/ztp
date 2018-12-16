from .text_handler import TextHandler


class Converter:

    def __init__(self, text_handler: TextHandler,
                 rules: dict, constants: dict, lookups: tuple) -> None:
        self.text_handler = text_handler
        self.rules = rules
        self.constants = constants
        self.lookups = lookups

    @property
    def transposed(self) -> str:
        return " ".join(self._convert())

    def _convert(self) -> list:
        result = []
        for word in self.text_handler.words:
            result.append(self._transpose(word))

        return result

    def _transpose(self, word: str) -> str:
        lowercase = word.lower()
        converted = []

        for i in range(len(word)):
            rule = self.rules.get(lowercase[i], word[i])

            if type(rule) == dict:
                result = None
                if rule.get('pre') and i > 0:  # TODO: Extract this i > 0 to a map between pre, post rules and their constraints
                    result = rule.get('pre').get(word[i-1])
                if rule.get('post') and i < len(word) - 1:
                    result = rule.get('post').get(word[i+1])
                if not result:
                    result = rule.get('other')
                rule = result

            converted.append(self._retain_uppercase(word[i], rule))

        return "".join(converted)

    def _retain_uppercase(self, original: str, copied: str) -> str:
        if original.isupper():
            return copied.upper()
        return copied