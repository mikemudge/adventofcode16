with open('advent20') as file:
    ranges = []
    for line in file.readlines():
        pieces = line[:-1].split('-')
        low = int(pieces[0])
        high = int(pieces[1])
        ranges.append((low, high))
    ranges.sort()
    print '\n'.join(str(x[0]) + '-' + str(x[1]) for x in ranges)

    lowestPossible = 0
    allowed = 0
    for r in ranges:
        print r[0], r[1]
        if lowestPossible < r[0]:
            # part 1
            # print 'Winner', lowestPossible
            # break

            # part 2
            print 'found allowed range', r[0] - lowestPossible, lowestPossible, r[0]
            allowed += r[0] - lowestPossible

        # Update the lowest possible to be larger then the current range max.
        if lowestPossible < r[1] + 1:
            lowestPossible = r[1] + 1
            # print 'updating lowest possible', r[0], r[1], lowestPossible

    # TODO could of had another range of allowed addresses here.
    print 4294967295 - lowestPossible, lowestPossible, 4294967295

    print 'addresses allowed', allowed
