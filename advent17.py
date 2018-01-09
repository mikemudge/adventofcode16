import hashlib

from collections import deque

def md5(s):
    h = hashlib.md5()
    h.update(s)
    return h.hexdigest()

def nextState(key, path, x, y):
    if key not in unlockKeys:
        return None
    if x < 1 or y < 1:
        return None
    if x > 4 or y > 4:
        return None
    if x == 4 and y == 4:
        # part 2
        solution['path'] = path
        # A path is complete when it reaches 4,4
        return None
        # part 1
        # raise Exception('Winner', path)
    return [path, x, y]

def getStates(state):
    path = state[0]
    x = state[1]
    y = state[2]
    doors = md5(passcode + path)
    result = []
    s = nextState(doors[0], path + 'U', x, y - 1)
    if s:
        result.append(s)
    s = nextState(doors[1], path + 'D', x, y + 1)
    if s:
        result.append(s)
    s = nextState(doors[2], path + 'L', x - 1, y)
    if s:
        result.append(s)
    s = nextState(doors[3], path + 'R', x + 1, y)
    if s:
        result.append(s)
    return result

def breadthFirst(state):
    queue = deque([startState])

    while queue:
        state = queue.popleft()
        # Add more states
        nextstates = getStates(state)

        [queue.append(s) for s in nextstates]

        print len(state[0]), len(queue)

    print 'Out of queue'

# Part 1
passcode = 'qzthpkfp'

# Testing
# passcode = 'hijkl'

unlockKeys = 'bcdef'
# path, x, y
startState = ['', 1, 1]
solution = {
    'path': ''
}

breadthFirst(startState)

print solution, len(solution['path'])
