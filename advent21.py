
def part1(lines, value):
    values = [value]
    for line in lines:
        pieces = line[:-1].split()
        if pieces[0] == 'swap':
            value = value[:]
            if pieces[1] == 'position':
                a = int(pieces[2])
                b = int(pieces[5])
                tmp = value[a]
                value[a] = value[b]
                value[b] = tmp
            elif pieces[1] == 'letter':
                a = pieces[2]
                b = pieces[5]
                done = 0
                for i in range(len(value)):
                    if value[i] == a:
                        value[i] = b
                        done += 1
                    elif value[i] == b:
                        value[i] = a
                        done += 1
                    if done == 2:
                        break
            else:
                raise Exception('Wrong')
        elif pieces[0] == 'rotate':
            if pieces[1] == 'left':
                rotate = int(pieces[2])
            elif pieces[1] == 'right':
                rotate = len(value) - int(pieces[2])
            elif pieces[1] == 'based':
                a = pieces[6]
                rotate = -1
                for i in range(len(value)):
                    if value[i] == a:
                        rotate = i + 1
                        if i >= 4:
                            rotate = (rotate + 1) % len(value)
                        break
                # Reverse the rotation direction.
                rotate = len(value) - rotate
            else:
                raise Exception('Wrong')
            value = value[rotate:] + value[:rotate]
        elif pieces[0] == 'reverse':
            a = int(pieces[2])
            b = int(pieces[4])
            middle = value[a:b + 1]
            middle.reverse()
            value = value[:a] + middle + value[b + 1:]
        elif pieces[0] == 'move':
            value = value[:]
            a = int(pieces[2])
            b = int(pieces[5])
            value.insert(b, value.pop(a))
        else:
            raise Exception('Wrong')

        values.append(value)
    return values

def part2(lines, value):
    values = [value]
    print value
    for line in lines:
        pieces = line[:-1].split()
        if pieces[0] == 'swap':
            value = value[:]
            if pieces[1] == 'position':
                a = int(pieces[2])
                b = int(pieces[5])
                tmp = value[a]
                value[a] = value[b]
                value[b] = tmp
            elif pieces[1] == 'letter':
                a = pieces[2]
                b = pieces[5]
                done = 0
                for i in range(len(value)):
                    if value[i] == a:
                        value[i] = b
                        done += 1
                    elif value[i] == b:
                        value[i] = a
                        done += 1
                    if done == 2:
                        break
            else:
                raise Exception('Wrong')
        elif pieces[0] == 'rotate':
            if pieces[1] == 'left':
                rotate = len(value) - int(pieces[2])
            elif pieces[1] == 'right':
                rotate = int(pieces[2])
            elif pieces[1] == 'based':
                a = pieces[6]
                # Assumes a value with length 8 because there is generic solutions don't exist for some numbers.
                # E.g both of these inputs result in the same output.
                # ecabd on d moved 6(1) right or 4 left. decab
                # abdec on d moved 3 right or 2 left. decab

                # initial, shift, result.
                # 0, 1, 1
                # 1, 2, 3
                # 2, 3, 5
                # 3, 4, 7
                # 4, 6, 2
                # 5, 7, 4
                # 6, 0, 6
                # 7, 1, 0
                shift = [
                    1,
                    1,
                    6,
                    2,
                    7,
                    3,
                    0,
                    4,
                ]

                size = len(value)
                for i in range(size):
                    if value[i] == a:
                        rotate = shift[i]
            else:
                raise Exception('Wrong')
            value = value[rotate:] + value[:rotate]
        elif pieces[0] == 'reverse':
            a = int(pieces[2])
            b = int(pieces[4])
            middle = value[a:b + 1]
            middle.reverse()
            value = value[:a] + middle + value[b + 1:]
        elif pieces[0] == 'move':
            value = value[:]
            a = int(pieces[2])
            b = int(pieces[5])
            value.insert(a, value.pop(b))
        else:
            raise Exception('Wrong')

        values.append(value)

    return values

with open('advent21') as file:
    lines = file.readlines()

    value = [x for x in 'abcdefgh']

    result = part1(lines, value)
    print 'part 1', ''.join(result[-1])
    print ''

    # Part 1
    # fchabged is wrong
    # abgcedfh is wrong
    # baecdfgh

    # Part 2 is reversed version of that for this result.
    value = [x for x in 'fbgdceah']

    # Handle the same lines backwards
    lines.reverse()
    result = part2(lines, value)
    size = len(result)

    print 'started with', ''.join(result[0])
    # for i in range(size - 1):
    #     print 'value', ''.join(result[i])
    #     print lines[i][:-1]
    print 'ended with', ''.join(result[-1])
    print ''

    # Re reverse the lines.
    lines.reverse()
    result2 = part1(lines, result[-1])

    print 'part 1 again'
    print 'starting with', ''.join(result2[0])
    # for i in range(1, size):
    #     print lines[i - 1][:-1]
    #     print 'value', ''.join(result2[i])
    print 'ended with', ''.join(result2[-1])
    print ''

    print 0, ''.join(result2[0]), ''.join(result[-1])
    for i in range(1, size):
        print lines[i - 1][:-1]
        # Prints what it should be vs what it was.
        # Forward pass with what part2 created.
        expected = ''.join(result2[i])
        got = ''.join(result[size - i - 1])
        print i, expected, got, '<--- wrong' if expected != got else ''
        if expected != got:
            break
