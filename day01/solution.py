from more_itertools import pairwise, windowed


def part1(input):
    res = 0
    for a, b in pairwise(input):
        if a < b:
            res += 1
    return res

def tmsums(input):
    for a in windowed(input, 3):
        yield sum(a)

def part2(input):
    sums = tmsums(input)
    return part1(sums)

def main():
    with open("day01/input.txt") as f:
        f_int = (int(a) for a in f)
        print(f"solution for part 1 is: {part1(f_int)}")
        f.seek(0)
        f_int = (int(a) for a in f)
        print(f"solution for part 2 is: {part2(f_int)}")

if __name__ == "__main__":
    main()