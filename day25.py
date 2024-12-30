from typing import Union
from time import perf_counter
from utils import Day
from collections import defaultdict


def part_one(data: list[str]) -> Union[str, int]:
    keys = []
    locks = []
    for elem in data:
        rows = elem.replace(".", "0").replace("#", "1").split()
        if rows[0] == "00000":
            keys.append([int(x,2) for x in rows[1:-1]])
        else:
            locks.append([int(x,2) for x in rows[1:-1]])
    tot = 0
    for lock in locks:
        for key in keys:
            valid = True
            for a,b in zip(lock, key):
                valid &= not a & b
            tot += valid

    return tot


def main():
    test_case_1 = """#####
.####
.####
.####
.#.#.
.#...
.....

#####
##.##
.#.##
...##
...#.
...#.
.....

.....
#....
#....
#...#
#.#.#
#.###
#####

.....
.....
#.#..
###..
###.#
###.#
#####

.....
.....
.....
#....
#.#..
#.#.#
#####"""

    test = False
    day = 25
    if test:
        print("TEST VALUES")
        data = test_case_1.strip().split("\n\n")
    else:
        data = Day.get_data(day).strip().split("\n\n")

    start = perf_counter()
    print(f"day {day} part 1: {part_one(data)}  in {perf_counter() - start:.4f}s")
    print(f"the whole day {day} took {perf_counter() - start:.4f}s")


main()
