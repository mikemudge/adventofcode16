import hashlib

fav = 'ahsbgdzn'

# Testing
# fav = 'abc'

def containsTrip(s):
    return containsConsec(s, 3)
def containsFiveInARow(s):
    return containsConsec(s, 5)

def containsConsec(s, t):
    count = 0
    last = 0
    for c in s:
        if c == last:
            count += 1
            if count == t - 1:
                return c
        else:
            count = 0
        last = c
    return None

def part2(s):
    for i in range(2016):
        h = hashlib.md5()
        h.update(s)
        s = h.hexdigest()
    return s

i = 0
endAt = 0
candidates = []
keys = []
while True:
    h = hashlib.md5()
    h.update(fav + str(i))
    m = h.hexdigest()
    m = part2(m)
    c2 = containsFiveInARow(m)
    if c2:
        print 'found 5', c2, m
        # check candidates for a match or more?
        # Remove any which are > 1000 away though.

        for ca in candidates:
            if i - ca[0] > 1000:
                # Remove these for performance?
                continue

            if ca[1] == c2:
                print 'match is a key', ca[0], 'and', i
                keys.append(ca[0])
                if len(keys) == 64:
                    # Need to go 1000 more incase there are other keys before this.
                    endAt = 1000 + ca[0]

    c = containsTrip(m)
    if c:
        candidates.append((i, c))

    i += 1
    # Need an end condition
    if endAt != 0 and i > endAt:
        break

keys.sort()
print keys

print keys[63]
