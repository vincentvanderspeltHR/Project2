i = int(input("Insert a number for height: "))
s = ''
width = 2 * i
for y in range(1, i + 1):
    for x in range(0, width):
        if x < i + y and x > i - y:
            s += '*'
        else:
            s += ' '
    s += '\n'
print(s)