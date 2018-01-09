with open('advent2') as f:
    x = 2
    y = 2
    letters = [
        [0, 0, 1, 0, 0],
        [0, 2, 3, 4, 0],
        [5, 6, 7, 8, 9],
        [0, 'A', 'B', 'C', 0],
        [0, 0, 'D', 0, 0],
    ]
    allowed = [
        [0, 0, 1, 0, 0],
        [0, 1, 1, 1, 0],
        [1, 1, 1, 1, 1],
        [0, 1, 1, 1, 0],
        [0, 0, 1, 0, 0]
    ]
    lines = f.readlines()
    for line in lines:
        line = line[:-1]
        for c in line:
            # print c, y, x, allowed[y][x]
            if c == 'U':
                if y - 1 >= 0 and allowed[y - 1][x]:
                    y = y - 1
            elif c == 'D':
                if y + 1 < 5 and allowed[y + 1][x]:
                    y = y + 1
            elif c == 'L':
                if x - 1 >= 0 and allowed[y][x - 1]:
                    x = x - 1
            elif c == 'R':
                if x + 1 < 5 and allowed[y][x + 1]:
                    x = x + 1
        print letters[y][x]
