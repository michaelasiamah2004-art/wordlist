def num_letters(num_rows,num_columns):
    return num_rows*(num_columns-1)


assert num_letters(1,5)==4
assert num_letters(4,4)==12
assert num_letters(2,10)==18
assert num_letters(5,7)==30

print("Checking assertions.")

import numpy as np
data = np.loadtxt("loop4.csv", delimiter=",", dtype=str, encoding = 'utf8')

words =[]
rows, columns = data.shape
cell = data[0,columns-1]
for r in range(rows):
    for c in range(columns):
        if cell == (''):
            continue
        else:
            words.append(str(data[r,c]))

print(words)
assert len(words) == rows*columns

two_words = []

for r in range(rows):
    for c in range(columns-1):
        word = data[r,c]+data[r,c+1]
        two_words.append(word)

print(two_words)
assert len(two_words)==num_letters(rows,columns)
