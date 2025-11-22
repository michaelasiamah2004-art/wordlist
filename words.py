def num_letters(num_rows, num_columns):
    return num_rows * (num_columns - 1)

assert num_letters(1, 5) == 4
assert num_letters(4, 4) == 12
assert num_letters(2, 10) == 18
assert num_letters(5, 7) == 30

print("Checking assertions.")

import numpy as np

data = np.loadtxt("loop4.csv", delimiter=",", dtype=str, encoding="utf8")

rows, columns = data.shape
words = []
r = 0
while r < rows:
    c = 0
    while c < columns:
        letter = str(data[r, c])
        if letter != "":
            words.append(letter)
        c += 1
    r += 1

print(words)



two_words = []
r = 0
while r < rows:
    c = 0
    while c < (columns - 1):

        first = data[r, c]
        second = data[r, c + 1]

        if first != "" and second != "":
            two_words.append(first + second)

        c += 1
    r += 1

print(two_words)

