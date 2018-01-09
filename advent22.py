def viableNodes(nodeA, nodes):
    num = 0
    for row in nodes:
        for nodeB in row:
            if nodeA == nodeB:
                continue
            if nodeA['used'] == 0:
                continue
            if nodeA['used'] <= nodeB['avail']:
                num += 1
    return num

def printArr(nodes):
    for row in nodes:
        print ','.join([str(a) for a in row])

with open('advent22') as file:
    lines = file.readlines()
    nodes = [[None for x in range(32)] for y in range(30)]
    board = [[None for x in range(32)] for y in range(30)]

    for i in range(2, len(lines)):
        pieces = lines[i][:-1].split()
        pos = pieces[0].split('-')
        x = int(pos[1][1:])
        y = int(pos[2][1:])

        # Size  Used   Avail
        # 85T   69T    16T
        size = int(pieces[1][:-1])
        used = int(pieces[2][:-1])
        avail = int(pieces[3][:-1])

        nodes[y][x] = {
            'size': size,
            'used': used,
            'avail': avail,
        }

    for row in nodes:
        print ','.join([(str(a['used']) + '/' + str(a['size'])) if a['used'] < 100 else '##/##' for a in row])

    count = 0
    print len(nodes), len(nodes[0])
    for y, row in enumerate(nodes):
        for x, node in enumerate(row):
            sum = viableNodes(node, nodes)
            count += sum

    print 'part 1', count

    for y, row in enumerate(nodes):
        for x, node in enumerate(row):
            if node['size'] > 100:
                board[y][x] = '#'
            elif node['used'] == 0:
                board[y][x] = '_'
            else:
                board[y][x] = '.'

    printArr(board)
    # Part 2.
    # Get data at y=0,x=31 to 0, 0 in fewest moves.
# Manually calculated.
# 31 moves to get 31 -> 30 with gap in 31.
# 50 moves to get 30 -> 20
# 50 moves to get 20 -> 10
# 50 moves to get 10 -> 0
