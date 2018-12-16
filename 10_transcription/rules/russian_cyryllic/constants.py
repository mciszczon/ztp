W = ("a", "е", "ё", "u", "o", "y", "э", "ю", "я")  # wovels
C = ("б", "в", "г", "д", "ж", "з", "й", "л", "м", "р", "с", "т", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь")  # consonants
HS = "ъ"  # hard sign
SS = "ь"  # soft sign
WS = "word start"
WE = "word end"

PRE = "pre"
POST = "post"
O = "other"

constants = { W, C, HS, SS, WS, WE }
lookups = (PRE, POST, O)