from collections import Counter
import string

dir = "/Users/homefolder/Desktop/Python/Green Belt/sprint4/sample.txt"
counter = 0
translator = str.maketrans('', '', string.punctuation)
with open(dir, 'r') as file:

    text = file.read()
    words = text.split()
new = []
for x in words:
    new.append(x.lower().translate(translator))
    

# count = len(words)
frequency = Counter(new)

for i, value in frequency.items():
    if value == 1:
        counter+=1

sorted = dict(sorted(frequency.items(), key=lambda item: item[1], reverse=True))
dict10=list(sorted.items())[:10]


print("Top 10 occuring words:")
for q, p in dict10:
    print(f"{q}: {p}")

# print(count)
# print(counter)
# print(sorted)
firstitem = next(iter(sorted.items()))
print(f"Most common word: {firstitem}")

