regs = {
    'a': 0,
    'b': 0,
    'c': 1,
    'd': 0
}

def getValue(regOrValue):
    try:
        value = int(regOrValue)
    except ValueError:
        value = regs[regOrValue]
    return value

with open('advent12') as f:
    lines = f.readlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        pieces = line.split()
        print pieces
        if pieces[0] == 'cpy':
            value = getValue(pieces[1])
            regId = pieces[2]
            regs[regId] = value
            print regId, '=', value
        elif pieces[0] == 'inc':
            regId = pieces[1]
            regs[regId] += 1
            print regId, '++', regs[regId]
        elif pieces[0] == 'dec':
            regId = pieces[1]
            regs[regId] -= 1
            print regId, '--', regs[regId]
        elif pieces[0] == 'jnz':
            value = getValue(pieces[1])
            if value != 0:
                i += int(pieces[2])
                print 'goto', pieces[2]
                continue
        else:
            raise Exception("nope")
        i += 1

    print 'a =', regs['a']
