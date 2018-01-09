
def formatScreen(screen):
    return '\n'.join([''.join(['#' if s2 else '_' for s2 in s]) for s in screen])

with open('advent8') as f:
    lines = f.readlines()
    count = 0
    count2 = 0
    screen = [[0] * 50 for i in range(6)]
    print formatScreen(screen)

    for line in lines:
        print line.strip()
        instruction = line.split()
        if instruction[0] == 'rect':
            # set pixels in rect
            height, width = instruction[1].split('x')
            print width, height
            for y in range(int(width)):
                for x in range(int(height)):
                    screen[y][x] = 1
        elif instruction[0] == 'rotate':
            # Which way?
            which = int(instruction[2].split('=')[1])
            # 3 is BY
            howMuch = int(instruction[4])
            if instruction[1] == 'column':
                rotated = [screen[(i - howMuch) % 6][which] for i in range(6)]
                for i in range(6):
                    screen[i][which] = rotated[i]
            elif instruction[1] == 'row':
                rotated = [screen[which][(i - howMuch) % 50] for i in range(50)]
                screen[which] = rotated
            else:
                print 'unknown instruction', instruction[1]
        else:
            print 'unknown instruction', instruction[0]
        print formatScreen(screen)
    print 'Final form'
    print formatScreen(screen)
    totalOn = sum([sum(x) for x in screen])
    print totalOn
