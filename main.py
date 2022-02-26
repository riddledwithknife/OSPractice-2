import hashlib
from time import time
from unicodedata import name

start = time()
n = int(input("Введите количество хэшей: "))
hash = []
for i in range(n):
    hash.append(input())

word = ""
letters = list("abcdefghijklmnopqrstuvwxyz")
result = {}
for l1 in letters:
    for l2 in letters:
        for l3 in letters:
            for l4 in letters:
                for l5 in letters:
                    word = bytes(l1 + l2 + l3 + l4 + l5, encoding='utf-8')
                    if hashlib.sha256(word).hexdigest() in hash:
                        result[hashlib.sha256(word).hexdigest()] = word
print(result)
end = time() - start
print(end)
