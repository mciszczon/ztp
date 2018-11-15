import re
from collections import Counter
import numpy

"""
TODO: OOP
TODO: Use import csv
"""

def get_result():
    with open('wiki.txt', 'r') as file:
        text = file.read().rstrip().replace("\n", " ").lower()
        d = Counter(re.compile('[,\.!?\(\)„”]').sub('', text).split(" "))

        print("Created list!")
        return  enumerate(sorted(d.items(), key=lambda kv: kv[1], reverse=True))

def write_file(result):
    with open('wiki.csv', 'w') as file:
        for i, item in result:
            file.writelines("{},{},{}\n".format(i+1, item[0], item[1]))
        else:
            print("Wrote to file!")

def count_const(result):
    numbers = [i * num[1] for i, num in result]
    print(sum(numbers)/len(numbers))

result = get_result()
write_file(result)

result = get_result()
count_const(result)


"""
HELPERS
"""

# import csv

# file  = 'wiki.txt'
# file_new = 'lista_frekwencyjna.csv'
# slownik = {}

# with open(file, 'r', encoding='utf8') as f:
#   for linia in f:
#     slowa = linia.split()
#     slowa = [item.lower().strip(',.;-_–%()[]{}+=&*$#@/\\!?\'"') for item in slowa]
#     for slowo in slowa:
#       if slowo:
#         if slowo not in slownik:
#           slownik[slowo] = 0
#         slownik[slowo] += 1

  
# with open(file_new, 'w', encoding='utf8') as f:
#   writer = csv.writer(f)
#   i=1
#   for w in sorted(slownik, key=slownik.get, reverse=True):
#     writer.writerow( (i, w, slownik[w]) )
#     i+=1
