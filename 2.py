import re
from collections import Counter
from PyGnuplot import s, pdf
import numpy

def get_result():
    with open('2.txt', 'r') as file:
        text = file.read().rstrip().replace("\n", " ").lower()
        d = Counter(re.compile('[,\.!?\(\)„”]').sub('', text).split(" "))

        print("Created list!")
        return  enumerate(sorted(d.items(), key=lambda kv: kv[1], reverse=True))

def write_file(result):
    with open('2.csv', 'w') as file:
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
