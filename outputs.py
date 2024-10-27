import os
countM, countT, count18 = 0, 0, 0
for file in os.listdir():
    formulas = []
    if file.startswith('output.txt'):
        with open(file, 'r') as f:
            content = f.readlines()
            countT+=int(content[0].split(": ")[1])
            countM += int(content[1].split(": ")[1])
            count18 += int(content[2].split(": ")[1])

lines = [f"Total: {countT} ", f"Monotonic: {countM} ", f"0-17: {count18} "]
# Open a file in write mode
with open(f"outputs.txt", "a") as file:
    # Write each line to the file
    file.writelines("\n".join(lines))