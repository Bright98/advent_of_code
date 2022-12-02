max_arr = []
prev_lines = 0

with open('input.txt') as file:
   for line in file:
      if line != "\n":
        prev_lines += int(line) 
      if line == '\n':
        max_arr.append(prev_lines)
        prev_lines = 0

max_arr.sort()
max_arr_len = len(max_arr)
print(max_arr[max_arr_len - 1] + max_arr[max_arr_len - 2] + max_arr[max_arr_len - 3])