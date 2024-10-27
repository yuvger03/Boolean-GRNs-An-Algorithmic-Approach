import os
import random
import sys
from monotonic_functions import is_monotonic_cnf
path = 'biodivine-boolean-models/models' #the BBM dataset is downloaded
os.chdir(path)
for i in random.sample(range(227), 150): # TODO: didnt do: 122,125-126,132,134,148,151,154,156-227
    dire = os.listdir()[i]
    if os.path.isdir(dire):
        os.chdir(dire)
        for file in os.listdir():
            if file.endswith('.bnet'):
                with open(file, 'rb') as f:
                    countM, countT = 0, 0
                    nonmono = []
                    content = f.readlines()  # Decode from bytes to string
                    for line in content[1:]:
                        line = line.decode('utf-8')
                        # Splitting by comma and extracting the right-hand side (the Boolean formula)
                        if ',' in line:
                            target, formula = line.strip().split(',', 1)
                            countT += 1
                            a, b, c, d = is_monotonic_cnf(formula)
                            if a and d is not None:
                                countM += 1
                            else:
                                nonmono.append(formula)
                    f.close()
                    os.chdir("..")
                    os.chdir("..")
                    os.chdir("..")
                    lines = [f"Total: {countT} ", f"Monotonic: {countM} ", f"not mono: {nonmono}"]
                    with open(f"output.txt{i}", "a") as file:
                        # Write each line to the file
                        file.writelines("\n".join(lines))
                    os.chdir(path)
