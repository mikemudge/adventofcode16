def checkAbba(s):
    containsAbba = False
    inSquares = False
    for i in range(len(s) - 3):
        if s[i] == '[':
            inSquares = True
            continue
        if s[i] == ']':
            inSquares = False
            continue
        if s[i] != s[i + 1] and s[i] == s[i + 3] and s[i + 1] == s[i + 2]:
            print s[i:i + 4], inSquares
            if inSquares:
                return False
            containsAbba = True
    return containsAbba

def checkAbaBab(s):
    inSquares = False
    abas = []
    babs = []
    for i in range(len(s) - 3):
        if s[i] == '[':
            inSquares = True
            continue
        if s[i] == ']':
            inSquares = False
            continue
        if s[i] != s[i + 1] and s[i] == s[i + 2]:
            print s[i:i + 3], inSquares
            if inSquares:
                babs.append(s[i:i + 3])
            else:
                abas.append(s[i:i + 3])
    # check if there is an aba which matches a bab.
    for aba in abas:
        for bab in babs:
            if bab[0] == aba[1] and bab[1] == aba[0]:
                print aba, bab
                return True
    return False

with open('advent7') as f:
    lines = f.readlines()
    count = 0
    count2 = 0
    for line in lines:
        if checkAbba(line):
            count += 1
        if checkAbaBab(line):
            count2 += 1
    print count, count2
