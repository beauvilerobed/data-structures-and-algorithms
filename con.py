# first get all lines from file
with open('numbers.txt', 'r') as f:
    lines = f.readlines()

# remove spaces
lines = [line.replace('\n', ', ') for line in lines]

# finally, write lines in the file
with open('file.txt', 'w') as f:
    f.writelines(lines)