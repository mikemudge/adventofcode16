from collections import deque
import itertools

def nextstate(queue, distances, moves, x, y):
    if x < 0 or y < 0:
        return
    if y >= height or x >= width:
        return
    if walls[y][x] == 1:
        # Can't walk through walls.
        return
    if distances[x][y] != -1:
        # Already visited this spot.
        return
    distances[x][y] = moves + 1
    queue.append((x, y))

def calculateDistances(point):
    distances = [[-1 for y in range(height)] for x in range(width)]
    distances[point[0]][point[1]] = 0

    queue = deque([point])

    while queue:
        state = queue.popleft()
        x = state[0]
        y = state[1]
        moves = distances[x][y]

        nextstate(queue, distances, moves, x - 1, y)
        nextstate(queue, distances, moves, x + 1, y)
        nextstate(queue, distances, moves, x, y - 1)
        nextstate(queue, distances, moves, x, y + 1)

    print queue

    return distances
def calculatePathLength(path, pointDistances):
    # Starting at 0 then going to each point in the order of path.
    dis = 0 + pointDistances[0][path[0]]
    for i in range(len(path) - 1):
        dis += pointDistances[path[i]][path[i + 1]]

    # Part 2
    # Move the robot back to 0 from where it ends up.
    dis += pointDistances[0][path[6]]

    return dis

with open('advent24') as f:
    lines = f.readlines()
    height = len(lines)
    width = len(lines[0]) - 1
    walls = [[0 for x in range(width)] for y in range(height)]
    points = {}
    for y, line in enumerate(lines):
        for x, c in enumerate(line[:-1]):
            if c == '#':
                walls[y][x] = 1
            if c in '0123456789':
                points[c] = (x, y)

    # distances = calculateDistances(points['7'])

    # for x, line in enumerate(distances):
    #     print ' '.join([('###' if walls[y2][x] == 1 else str(c).zfill(3) if c > -1 else '---') for y2, c in enumerate(line)])

    distanceBetweenPoints = []
    for p in range(len(points)):
        distances = calculateDistances(points[str(p)])
        distanceTo = []
        for p in range(len(points)):
            point = points[str(p)]
            x = point[0]
            y = point[1]
            distanceTo.append(distances[x][y])
        distanceBetweenPoints.append(distanceTo)

    for row in distanceBetweenPoints:
        print ', '.join([str(d).zfill(4) for d in row])

    shortestDistance = -1
    shortestPath = []
    for path in itertools.permutations(range(1, 8), 7):
        d = calculatePathLength(path, distanceBetweenPoints)
        if shortestDistance == -1 or d < shortestDistance:
            shortestDistance = d
            shortestPath = path

    print shortestDistance, shortestPath
