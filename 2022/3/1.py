def convert_lower_case(char):
    return ord(char) - 96

def convert_upper_case(char):
    return ord(char) - 38

def convert_char(char:str):
    if char.islower():
        return convert_lower_case(char)
    else:
        return convert_upper_case(char)

def split_half_of_string(string:str):
    first_half  = string[:len(string)//2]
    second_half = string[len(string)//2:]
    return first_half, second_half

def find_similar_char(str1, str2):
    return str(list(set(str1) & set(str2))[0])

count = 0

with open('input.txt') as file:
    for line in file:
        line = line.replace("\n", "")
        first_half, sec_half = split_half_of_string(line)
        count += convert_char(find_similar_char(first_half, sec_half))

print(count)