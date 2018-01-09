
def part1():
    # Assumes a 0 based elf index.
    nextElves = range(1, numberOfElves + 1)
    nextElves[numberOfElves - 1] = 0

    currentElf = 0

    while True:
        nextElf = nextElves[currentElf]
        nextNextElf = nextElves[nextElf]

        if currentElf == nextNextElf:
            # When there is only one elf left its over.
            break

        # nextElf loses all his presents
        nextElves[nextElf] = -1
        # The currentElf updates his next elf to the one after.
        nextElves[currentElf] = nextNextElf

        # Now move around the circle
        currentElf = nextNextElf

    # Because elfs use a 1 based index and the array uses a 0 based index.
    print currentElf + 1, 'gets all the presents'

def part2():
    # Assumes a 0 based elf index.
    nextElves = range(1, numberOfElves + 1)
    nextElves[numberOfElves - 1] = 0

    # minus one because we need to track the elf before the removed one.
    # This is so we can update the linked list to skip the removed one.
    currentElf = numberOfElves / 2 - 1

    count = numberOfElves
    # Single deletions of a list isn't very fast with large lists.
    # Could improve performance significantly.
    while True:
        print count
        # , nextElves
        nextElf = nextElves[currentElf]
        nextNextElf = nextElves[nextElf]

        if currentElf == nextNextElf:
            # When there is only one elf left its over.
            break

        count -= 1
        nextElves[nextElf] = -1
        nextElves[currentElf] = nextNextElf

        if count % 2 == 0:
            # Due to the nature of tracking opposites with a reducing circle size we only increment this half the time.
            currentElf = nextElves[currentElf]

    # There should only be 1 elf left.
    print currentElf + 1, 'gets all the presents'


numberOfElves = 3014603

# Testing
# numberOfElves = 5

# part1()

part2()
