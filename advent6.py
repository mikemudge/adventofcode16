import operator

with open('advent6') as f:
    lines = f.readlines()
    print lines
    allLetters = [{}, {}, {}, {}, {}, {}, {}, {}]
    for line in lines:
        for i in range(len(line) - 1):
            letterCounts = allLetters[i]
            let = line[i]
            print i, let, letterCounts.get(let, 0)
            letterCounts[let] = letterCounts.get(let, 0) + 1

    result = []
    for i in range(len(line) - 1):
        letterCounts = allLetters[i]
        lst = sorted(letterCounts.items(), key=operator.itemgetter(1))
        print '--'
        print i, lst
        result.append(lst[0][0])
    print ''.join(result)
