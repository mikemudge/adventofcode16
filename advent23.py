regs = {
    'a': 7,
    'b': 0,
    'c': 0,
    'd': 0
}
# part 2
regs['a'] = 12

def getValue(regOrValue):
    try:
        value = int(regOrValue)
    except ValueError:
        value = regs[regOrValue]
    return value

def switchInstruction(line):
    pieces = line.split()
    print 'before', pieces
    # TODO switch
    if pieces[0] == 'tgl':
        pieces[0] = 'inc'
    elif pieces[0] == 'cpy':
        pieces[0] = 'jnz'
    elif pieces[0] == 'inc':
        pieces[0] = 'dec'
    elif pieces[0] == 'dec':
        pieces[0] = 'inc'
    elif pieces[0] == 'jnz':
        pieces[0] = 'cpy'

    print 'after', pieces

    return ' '.join(pieces)

with open('advent23') as f:
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
        if pieces[0] == 'tgl':
            offset = getValue(pieces[1])
            print i, 'tgl', offset
            offset += i
            if offset >= 0 and offset < len(lines):
                lines[offset] = switchInstruction(lines[offset])
            # What next?
        elif pieces[0] == 'cpy':
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
        else:
            raise Exception("nope")
        i += 1

    print 'final a =', regs['a']
