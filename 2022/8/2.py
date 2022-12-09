lines = open("input.txt", "r").readlines()
# lines = ['30373', '25512', '65332', '33549', '35390']

def check_left(array, index): 
    count = 0
    left_index = index
    while left_index > 0:
        if int(array[left_index - 1]) < int(array[index]):
            left_index -= 1
            count += 1
        else:
            count +=1
            break
    return count


def check_right(array, index):
    count = 0
    right_index = index
    while right_index < len(array) - 1:
        if int(array[right_index + 1]) < int(array[index]):
            right_index += 1
            count += 1
        else:
            count +=1
            break
    return count


def check_top(array, index1, index2): 
    count = 0
    top_index = index1
    while top_index > 0:
        if int(array[top_index - 1][index2]) < int(array[index1][index2]):
            top_index -= 1
            count += 1
        else:
            count +=1
            break
    return count


def check_bottom(array, index1, index2): 
    count = 0
    bottom_index = index1
    while bottom_index < len(array) - 1:
        if int(array[bottom_index + 1][index2]) < int(array[index1][index2]):
            bottom_index += 1
            count += 1
        else:
            count +=1
            break
    return count


maximum = 0
for i in range(1, len(lines) - 1):
    lines[i] = lines[i].replace("\n", "")
    
    for j in range(1, len(lines[i]) - 1):
        right = check_left(lines[i], j)
        left = check_right(lines[i], j)
        top = check_top(lines, i, j)
        bottom = check_bottom(lines, i, j)

        mult = left * right * top * bottom
        if mult > maximum:
            maximum = mult


print(maximum)
