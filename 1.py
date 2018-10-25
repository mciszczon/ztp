first = 20
last = 200000000

""" Wersja list comprehension, mniej optymalna """
# print([num for num in range(first, last+1) if not [part for part in str(num) if int(part) % 2 != 0]])

""" Wersja zoptymalizowana """
for number in range(first, last+1):
    for part in tuple(str(number)):
        if int(part) % 2 != 0: break
    else: print(number)