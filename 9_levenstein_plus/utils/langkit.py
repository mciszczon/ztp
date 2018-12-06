from .bidict import BiDict

digraphs = {
    'ch': 'H',
    'rz': 'Ż',
}

diacritics = BiDict({
    'a': 'ą',
    'c': 'ć',
    'e': 'ę',
    'l': 'ł',
    'n': 'ń',
    'o': 'ó',
    's': 'ś',
    'z': 'ź',
})

ortographics = BiDict({
    'u': 'ó'
})