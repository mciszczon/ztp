from collections import OrderedDict
from rules.russian_cyryllic.constants import W, C, SS, HS, WS, O, WE, PRE, POST
from rules.russian_cyryllic.constants import constants, lookups


russian_cyryllic = {
    "а": "a",
    "б": "b",
    "в": "w",
    "г": "g",
    "д": "d",
    "е": {
        PRE: OrderedDict({
            W: "je",
            SS: "je",
            HS: "je",
            "ж": "e",
            "л": "e",
            "ц": "e",
            "ч": "e",
            "ш": "e",
            "щ": "e",
        }),
        O: "ie",
    },
    "ё": {
        PRE: OrderedDict({
            WS: "jo",
            W: "jo",
            HS: "jo",
            SS: "jo",
            "ж": "o",
            "л": "o",
            "ч": "o",
            "ш": "o",
            "щ": "o",
        }),
        O: "io",
    },
    "ж": "ż",
    "з": "z",
    "и": {
        PRE: OrderedDict({
            SS: "ji",
            "ж": "y",
            "ц": "y",
            "ш": "y",
        }),
        O: "i",
    },
    "й": "j",
    "к": "k",
    "л": {
        POST: OrderedDict({
            "е": "l",
            "ё": "l",
            "и": "l",
            "ь": "l",
            "ю": "l",
            "я": "l",
            C: "ł",
            "а": "ł",
            "о": "ł",
            "у": "ł",
            "ы": "ł",
            WE: "ł"
        }),
        O: "l",
    },
    "м": "m",
    "н": "n",
    "о": "o",
    "п": "p",
    "р": "r",
    "с": "s",
    "т": "t",
    "у": "u",
    "f": "ф",
    "х": "ch",
    "ц": "c",
    "ч": "cz",
    "ш": "sz",
    "щ": "szcz",
    "ъ": "",
    "ы": "y",
    "ь": {
        PRE: OrderedDict({
            "л": "",
            "ж": "",
            "ш": "",
            "ч": "",
            "щ": "",
        }),
        POST: OrderedDict({
            W: "",
        }),
        O: "ʹ",
    },
    "э": "e",
    "ю": "ju",  # TODO
    "я": "ja",  # TODO
}
