import heapq

fav = 1362
def valueFunc(x, y):
    v = x * x + 3 * x + 2 * x * y + y + y * y
    v += fav
    b = bin(v)[2:]
    tot = sum([int(a) for a in b])
    return tot % 2

for y in range(39):
    line = ['S' if x == 31 and y == 39 else '#' if valueFunc(x, y) else ' ' for x in range(31)]
    print ''.join(line)

startState = {
    'x': 1,
    'y': 1,
    'turns': 0
}
heap = []
heapq.heappush(heap, (0, startState))

visited = [[-1 for a in range(100)] for a in range(100)]
def addHeap(heap, state):
    x = state['x']
    y = state['y']
    if x == 31 and y == 39:
        raise Exception('I win %s' % state['turns'])
    if x >= 0 and y >= 0:
        if visited[x][y] != -1:
            print x, y, visited[x][y]
            # skip this because we already been here?
            return
        if not valueFunc(x, y):
            pri = state['x'] + state['y'] + state['turns']
            # Just use turns for part 2.
            pri = state['turns']
            heapq.heappush(heap, (pri, state))
            visited[state['x']][state['y']] = state['turns']
        else:
            # Been to but its a wall.
            visited[state['x']][state['y']] = -2

visited[startState['x']][startState['y']] = 0
try:
    while heap:
        cost, state = heapq.heappop(heap)
        print cost, state

        addHeap(heap, {
            'x': state['x'] + 1,
            'y': state['y'],
            'turns': state['turns'] + 1
        })
        addHeap(heap, {
            'x': state['x'] - 1,
            'y': state['y'],
            'turns': state['turns'] + 1
        })
        addHeap(heap, {
            'x': state['x'],
            'y': state['y'] + 1,
            'turns': state['turns'] + 1
        })
        addHeap(heap, {
            'x': state['x'],
            'y': state['y'] - 1,
            'turns': state['turns'] + 1
        })
except Exception as e:
    print e
    pass
# Count number of visited with < 50
count = 0
for y in range(100):
    for x in range(100):
        # If visited and < 50 turns away.
        if visited[x][y] >= 0 and visited[x][y] <= 50:
            count += 1
    print ''.join(['##' if v == -2 else str(v).zfill(2) for v in visited[y]])

print "Number of squares reachable in 50 is", count

# Part 2
# 322 too high
# 133 too low
# 137 is wrong.
