
def generateData(start):
    reverse = start[::-1]
    # TODO invert 0,1s in reverseInvert.
    reverseInvert = ''.join(['0' if c == '1' else '1' for c in reverse])
    return start + '0' + reverseInvert

def calculateCrc(data):
    result = []
    for i in range(0, len(data), 2):
        if data[i] == data[i + 1]:
            result.append('1')
        else:
            result.append('0')
    return ''.join(result)

# Part 1
length = 272
data = '11100010111110100'
# Part 2
length = 35651584

# Testing
# length = 20
# data = '10000'

while len(data) < length:
    data = generateData(data)
    print 'data', len(data)

# Remove any extra data
data = data[:length]
# print 'data', data

crc = data
while len(crc) % 2 == 0:
    crc = calculateCrc(crc)
    print 'crc', len(crc)

print 'crc', crc
