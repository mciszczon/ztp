"""
1. Tworzę 1-, 2-, 3-gramy (może być więcej) dla obu porównywanych języków (tekstów). W ten sposób powstaje `x` i `y`.
   Porównuję tylko ngramy o takiej samej krotności! Czyli 1-gramy `x` z 1-gramami `y` itd.
   Są one częścią tego samego wektora, np. { 'a': 312, ..., 'ab': 12, ... }
2. x1 i y1 to odpowiadające sobie ngramy, np. 'al' i 'al' – a dokładniej ich wartości (częstością występowania).
3. Jeżeli dany ngram nie wystąpi w drugim tekście, to jego wartość powinna być przyjęta jako 0.

Długość wektora len(x): √x1^2 + x2^2 + x3^2 + ... + xn^2 (pierwiastek nad całością)
"""
