max = 0
prev_lines = 0

with open('input.txt') as file:
   for line in file:
      if line != "\n":
        prev_lines += int(line) 
      if line == '\n':
        if prev_lines > max:
            max = prev_lines
        prev_lines = 0

print(max)