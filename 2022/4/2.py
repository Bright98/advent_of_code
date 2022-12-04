def create_list(start, end):
    return list(range(int(start), int(end) + 1))


def check_lists_overlap(list1, list2):
    return len(list(set(list1) & set(list2))) != 0

count = 0

with open('input.txt') as file:
    for line in file:
        line = line.replace("\n", "")
        first, second = line.split(',')
        start, end = first.split("-")
        first_list = create_list(start, end)
        start, end = second.split("-")
        second_list = create_list(start, end)

        if check_lists_overlap(first_list, second_list):
            count +=1

print(count)