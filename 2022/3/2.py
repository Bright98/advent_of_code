def convert_lower_case(char):
    return ord(char) - 96

def convert_upper_case(char):
    return ord(char) - 38

def convert_char(char:str):
    if char.islower():
        return convert_lower_case(char)
    else:
        return convert_upper_case(char)

def find_similar_char(str1, str2, str3):
    return str(list(set(str1) & set(str2) & set(str3))[0])

count = 0

lines = open("input.txt", "r").readlines()
for i in range(len(lines)):
    if i % 3 == 0:
        first = lines[i].replace("\n", "")
        second = lines[i+1].replace("\n", "")
        third = lines[i+2].replace("\n", "")
        count += convert_char(find_similar_char(first, second, third))

print(count)