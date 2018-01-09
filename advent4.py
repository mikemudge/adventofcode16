
def calcCrc(s):

    letterMap = {}
    for l in s:
        letterMap[l] = letterMap.get(l, 0) + 1

    def sorter(item, item2):
        diff = item2[1] - item[1]
        if diff == 0:
            return 1 if item[0] > item2[0] else -1
        return diff

    lst = letterMap.items()
    lst.sort(sorter)

    result = ''.join([l[0] for l in lst[:5]])
    return result

def realRoom(s):
    # Find letters
    where = s.rfind('-')
    roomId, expectedCrc = s[where + 1:-1].split('[')
    letters = ''.join(s[:where].split('-'))

    # print s
    # print s[:where], roomId, expectedCrc
    actualCrc = calcCrc(letters)
    # print actualCrc, expectedCrc, actualCrc == expectedCrc, int(roomId)
    if actualCrc == expectedCrc:
        decrypted = ''.join([chr(97 + (ord(l) - 97 + int(roomId)) % 26) for l in letters])
        if 'northpoleobjectstorage' == decrypted:
            print 'Room', roomId, decrypted
        return int(roomId)
    return 0

with open('advent4') as f:
    lines = f.readlines()

    count = 0
    for line in lines:
        count += realRoom(line.strip())
    print 'total', count
    # 116875 is too low.
    # 137896?
