i = int(input("Insert a number for height: "))
s = ''
for y in range(0, i):
    for x in range(0, i):
    for x in range(0, width):
        if x < i + y and x > i - y:
            s += '*'
        else:
            s += ' '
    s += '\n'
print(s)