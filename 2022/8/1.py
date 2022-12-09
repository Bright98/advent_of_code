def check_from_left(array, number, index):
    list2 = array[0:index]
    return all(number > int(item) for item in list2)

def check_from_right(array: list, number, index):
    list2 = array[index + 1: len(array)]
    return all(number > int(item) for item in list2)

def check_from_top(array: list, number, first_index, index):
    list2 = []
    for k in range(first_index):
        list2.append(array[k][index])
    return all(number > int(item) for item in list2)

def check_from_bottom(array: list, number, first_index, index):
    list2 = []
    for k in range(first_index + 1, len(array)):
        list2.append(array[k][index])
    return all(number > int(item) for item in list2)

count = 0
lines = open("input.txt", "r").readlines()

for i, line in enumerate(lines):

    lines[i] = line.replace("\n", "")
    line = line.replace("\n", "")

    for j, number in enumerate(line):
        # check from left
        from_left = check_from_left(line, int(number), j)
        if from_left :
            count += 1
        
        else:
            # check from right
            from_right = check_from_right(line, int(number), j)
            if from_right:
                count += 1
            else:

                # check from top
                from_top = check_from_top(lines, int(number), i, j)
                if from_top:
                    count +=1
                else:

                    # check from bottom
                    from_bottom = check_from_bottom(lines, int(number), i, j)
                    if from_bottom:
                        count +=1

print(count)