import heapq

# The first floor contains a thulium generator, a thulium-compatible microchip, a plutonium generator, and a strontium generator.
# The second floor contains a plutonium-compatible microchip and a strontium-compatible microchip.
# The third floor contains a promethium generator, a promethium-compatible microchip, a ruthenium generator, and a ruthenium-compatible microchip.
# The fourth floor contains nothing relevant.

def printLevel(level):
    for i in range(3, -1, -1):
        result = []
        for k, v in startState.iteritems():
            if v == i:
                result.append(k)
            else:
                result.append('.' * len(k))
        print ', '.join(result)

def calcValue(level):
    # Things on level 1 are 3 moves away minimum.
    # Things on level 2 are 2 moves away etc.
    # Elevator position is irrelevant.
    return 0

floors = [
    ["E", "TG", "TM", "PG", "..", "SG", "..", "...", "...", "..", ".."],
    [".", "..", "..", "..", "PM", "..", "SM", "...", "...", "..", ".."],
    [".", "..", "..", "..", "..", "..", "..", "PRG", "PRM", "RG", "RM"],
    [".", "..", "..", "..", "..", "..", "..", "...", "...", "..", ".."]
]

3 * 4 = 12
2 * 2 = 4
1 * 4 = 4

20 * 2 - 9 (3 * 3)

startState = {}
for i, l in enumerate(floors):
    for thing in l:
        if '.' in thing:
            continue
        startState[thing] = i

print startState
printLevel(startState)

# Get everything to level 4.

calcValue(startState)

heap = []
heapq.heappush(heap, startState)

while heap:
    item = heapq.heappop(heap)
    # Calculate next states and heappush them.
    elevatorLevel = startState["E"]
    possibles = []
    for k, v in item.iteritems():
        if k == "E" or v != elevatorLevel:
            continue
        possibles.append(k)

    # move 1 or 2 of the possibles up or down.
    # Make sure not to leave the state of this level or the new one broken.
    # Add new states.
    # G's need to know about their M's and vice versa
    print possibles

print "Winner"
printLevel(item)
