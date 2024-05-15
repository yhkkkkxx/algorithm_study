test = int(input())
for t in range(test):

    teststr = list(input())

    table = []
    for i in range(65, 91): table.append(chr(i))
    for i in range(97, 123): table.append(chr(i))
    for i in range(48, 58): table.append(chr(i))
    table.append("+")
    table.append("/")

    buffer = ''
    for s in teststr: buffer += format(table.index(s), 'b').zfill(6)

    originalstr = []
    while buffer:
        originalstr.append(buffer[:8])
        buffer = buffer[8:]

    original = ''
    for s in originalstr:
        original+=chr(int("0b"+s, 2))

    print(f"#{t+1} {original}")