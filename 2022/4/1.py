def create_list(start, end):
    return list(range(int(start), int(end) + 1))

def check_sublist_of_list(bigger_list, sub_list):
    return all(x in bigger_list for x in sub_list)

def check_sublist(list1, list2):
    if len(list1) > len(list2):
        return check_sublist_of_list(list1, list2)
    else:
        return check_sublist_of_list(list2, list1)


count = 0

with open('input.txt') as file:
    for line in file:
        line = line.replace("\n", "")
        first, second = line.split(',')
        start, end = first.split("-")
        first_list = create_list(start, end)
        start, end = second.split("-")
        second_list = create_list(start, end)

        if check_sublist(first_list, second_list):
            count +=1

print(count)