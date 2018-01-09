tests = [
    ['ADVENT', 'ADVENT', 6],
    ['A(1x5)BC', 'ABBBBBC', 7],
    ['(3x3)XYZ', 'XYZXYZXYZ', 9],
    ['A(2x2)BCD(2x2)EFG', 'ABCBCDEFEFG', 11],
    ['(6x1)(1x3)A', '(1x3)A', 6],
    ['X(8x2)(3x3)ABCY', 'X(3x3)ABC(3x3)ABCY', 18],
]

tests2 = [
    ['(3x3)XYZ', 'XYZXYZXYZ', 9],
    ['X(8x2)(3x3)ABCY', 'XABCABCABCABCABCABCY', 20],
    ['(27x12)(20x12)(13x14)(7x10)(1x12)A', 'Um?', 241920],
    ['(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN', 'Um?', 445],
]

def decompress(line):
    decompressedLength = 0
    i = 0
    while (i < len(line)):
        if line[i] == '(':
            # Handle the repeat thing.
            repeat = line[i + 1: line.index(')', i)]
            print repeat, len(repeat)
            length, times = repeat.split('x')
            # Skip over the repeat description
            i += len(repeat) + 2
            # Skip over the repeated part.
            i += int(length)

            # Now add the length of the decompressed data
            decompressedLength += int(length) * int(times)
        else:
            # Normal character
            i += 1
            decompressedLength += 1
    return decompressedLength

def decompress2(line):
    decompressedLength = 0
    i = 0
    while (i < len(line)):
        if line[i] == '(':
            # Handle the repeat thing.
            nextBrack = line.index(')', i)
            repeat = line[i + 1: nextBrack]
            print 'found a repeat', repeat
            length, times = repeat.split('x')
            # Skip over the repeat description
            i += len(repeat) + 2

            repeatedString = line[nextBrack + 1: nextBrack + 1 + int(length)]
            print repeatedString
            repeatedStringLength = decompress2(repeatedString)
            print repeatedStringLength
            # Skip over the repeated part.
            i += int(length)

            # Now add the length of the decompressed data
            decompressedLength += repeatedStringLength * int(times)
        else:
            # Normal character
            i += 1
            decompressedLength += 1
    return decompressedLength

with open('advent9') as f:
    lines = f.readlines()

    # part 2 tests
    for test in tests2:
        result = decompress2(test[0])
        print test[0], 'expected', test[2], 'got', result
        if test[2] != result:
            raise Exception('Wrong')

    # part 1 tests
    for test in tests:
        result = decompress(test[0])
        print test[0], 'expected', test[2], 'got', result
        if test[2] != result:
            raise Exception('Wrong')

    for line in lines:
        d = decompress(line)
        d2 = decompress2(line)
        print 'total', d
        print 'total2', d2
