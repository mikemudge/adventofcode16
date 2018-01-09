with open('advent3') as f:
    lines = f.readlines()
    count = 0
    for i, line in enumerate(lines):
        line = line[:-1]
        values = [[], [], []]
        for w in line.split(' '):
            if w:
                values[i % 3].append(int(w))
        values.sort()
        if i % 3 == 2:
            if values[0] + values[1] > values[2]:
                count += 1
    print count
