# first get all lines from file
with open('', 'r') as f:
    lines = f.readlines()

# remove spaces
lines = [line.replace('\n', ',') for line in lines]

# finally, write lines in the file
with open('', 'w') as f:
    f.writelines(lines)