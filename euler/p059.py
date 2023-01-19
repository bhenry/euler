from pathlib import Path

data_folder = Path("euler/inputs/")
file_to_open = data_folder / "p059_cipher.txt"
with open(file_to_open) as f: input = f.read()

for i in range(97, 123):
    for j in range(97, 123):
        for k in range(97, 123):
            key = [i, j, k]
            output = ""
            inp = input.split(",")
            for n, char in enumerate(inp):
                output += chr(int(char) ^ key[n % 3])
            if " the " in output:
                print(output)
                print(sum([ord(c) for c in output]))
