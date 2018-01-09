# Disc #1 has 17 positions; at time=0, it is at position 5.
# Disc #2 has 19 positions; at time=0, it is at position 8.
# Disc #3 has 7 positions; at time=0, it is at position 1.
# Disc #4 has 13 positions; at time=0, it is at position 7.
# Disc #5 has 5 positions; at time=0, it is at position 1.
# Disc #6 has 3 positions; at time=0, it is at position 0.

# disc1 will be at 0 at the following times.

discs = [
    [1, 17, 5],
    [2, 19, 8],
    [3, 7, 1],
    [4, 13, 7],
    [5, 5, 1],
    [6, 3, 0],
    [7, 11, 0],
]

def willAlign(disc, time):
    # disc[0] is the time it takes for the ball to fall to the disc.
    # disc[2] is the initial position of the disc.
    pos = time + disc[0] + disc[2]
    # disc[1] is the number of positions for the disc.
    pos %= disc[1]

    # The ball will pass through if the disc is at position 0.
    return pos == 0

time = 0
while True:
    passed = 0
    for disc in discs:
        if willAlign(disc, time):
            passed += 1
    if passed > 4:
        print 'dropping at ', time, 'will get through', passed, 'discs'
    if passed == 7:
        # Found a winner
        break
    time += 1
