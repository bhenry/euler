from pathlib import Path

data_folder = Path("euler/inputs/")
file_to_open = data_folder / "p042_words.txt"
with open(file_to_open) as f: input = f.read()

words = input.split(",")

def wordvalue(word):
    return sum(ord(c)-64 for c in word)

def is_triangle(n):
    return (8*n+1)**0.5 % 1 == 0

c = [word for word in words if is_triangle(wordvalue(word.strip('"')))]
print(len(c))
