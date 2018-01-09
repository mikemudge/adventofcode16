regs = {
    'a': 198,
    'b': 0,
    'c': 0,
    'd': 0
}

def getValue(regOrValue):
    try:
        value = int(regOrValue)
    except ValueError:
        value = regs[regOrValue]
    return value

def runProgram():
    lines = f.readlines()
    i = 0
    count = 0
    while i < len(lines):
        count += 1
        # if count > 950:
        #     break
        line = lines[i]
        pieces = line.split()
        # print pieces
        if pieces[0] == 'cpy':
            value = getValue(pieces[1])
            regId = pieces[2]
            regs[regId] = value
            # print i, regId, '=', value
        elif pieces[0] == 'inc':
            regId = pieces[1]
            regs[regId] += 1
            # print i, regId, '++', regs[regId]
        elif pieces[0] == 'dec':
            regId = pieces[1]
            regs[regId] -= 1
            # print i, regId, '--', regs[regId]
        elif pieces[0] == 'jnz':
            value = getValue(pieces[1])
            if value != 0:
                offset = getValue(pieces[2])
                # print i, 'goto', pieces[2], offset
                i += offset
                continue
            # else:
                # print i, 'skip goto', pieces[2], pieces[1], '== 0'
        elif pieces[0] == 'out':
            # clock stuff
            print pieces[1], getValue(pieces[1])
        else:
            raise Exception("nope")
        i += 1

    print 'final a =', regs['a']

with open('advent25') as f:
    print bin(2532)[2:]
    # 100111100100
    # 101010101010
    print int('101010101010', 2)
    print 2730 - 2532

    # Just to test my workings.
    runProgram()
