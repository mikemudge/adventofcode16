
def calculateTrap(left, middle, right):
    if left and middle and not right:
        return True
    if not left and middle and right:
        return True
    if left and not middle and not right:
        return True
    if not left and not middle and right:
        return True
    return False

# Testing
startInput = '.^^.^.^^^^'
rows = 10

# Part 1
startInput = '^..^^.^^^..^^.^...^^^^^....^.^..^^^.^.^.^^...^.^.^.^.^^.....^.^^.^.^.^.^.^.^^..^^^^^...^.....^....^.'
rows = 40

# Part 2
# rows = 400000

row = [x == '^' for x in startInput]
width = len(row)
totalTraps = sum(row)
print '00' + ''.join(['^' if x else '.' for x in row])

for r in range(1, rows):
    nextrow = [0 for x in row]
    for i in range(width):
        left = row[i - 1] if i > 0 else 0
        middle = row[i]
        right = row[i + 1] if i + 1 < width else 0
        nextrow[i] = calculateTrap(left, middle, right)
        if nextrow[i]:
            totalTraps += 1

    print str(r).zfill(2) + ''.join(['^' if x else '.' for x in nextrow])
    row = nextrow

print 'safe tiles', rows * width - totalTraps

# 1984 is too low
