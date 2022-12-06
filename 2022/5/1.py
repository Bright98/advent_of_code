import re

list1 = []
list2 = []
list3 = []
list4 = []
list5 = []
list6 = []
list7 = []
list8 = []
list9 = []

map_list =  {
    '1': list1,
    '2': list2,
    '3': list3,
    '4': list4,
    '5': list5,
    '6': list6,
    '7': list7,
    '8': list8,
    '9': list9,
}

def fill_array(array:list, item):
    if item != " ":
        array.append(item)
    return array

lines = open("input.txt", "r").readlines()
for i in range(8):
    rev_index = 7 - i
    list1 = fill_array(list1, lines[rev_index][1])
    list2 = fill_array(list2, lines[rev_index][5])
    list3 = fill_array(list3, lines[rev_index][9])
    list4 = fill_array(list4, lines[rev_index][13])
    list5 = fill_array(list5, lines[rev_index][17])
    list6 = fill_array(list6, lines[rev_index][21])
    list7 = fill_array(list7, lines[rev_index][25])
    list8 = fill_array(list8, lines[rev_index][29])
    list9 = fill_array(list9, lines[rev_index][33])


def move_box(order:list):
    move = -int(order[0])
    movement = map_list[order[1]][move: len(map_list[order[1]])]
    map_list[order[1]] = map_list[order[1]][:move]
    map_list[order[2]].extend(reversed(movement))

    return map_list[order[1]]


for i in range(10, len(lines)):
    lines[i] = lines[i].replace("\n", "")
    order = re.findall(r'\d+', lines[i])
    map_list[order[1]] = move_box(order)

string = ''
for lists in map_list:
    string += map_list[lists].pop()

print(string)