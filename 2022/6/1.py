lines = open("input.txt", "r").readlines()
line = lines[0].replace("\n", "")

for i in range(4, len(line)):
    if len(set(line[i - 4: i])) == 4:
        print(i)
        break
