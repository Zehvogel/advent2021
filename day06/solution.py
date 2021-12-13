import time


def calc(input, days):
    t0 = time.perf_counter_ns()
    n = 9
    state = [0] * n
    for i in range(n):
        state[i] = input.count(str(i))

    for d in range(days):
        new_fish = state[0]
        for i, s in enumerate(state):
            if i == 0:
                continue
            state[i-1] = s
        state[6] += new_fish
        state[8] = new_fish
    t1 = time.perf_counter_ns()
    print(f"calculation took {t1 - t0} ns")
    return sum(state)

def part1(input):
    return calc(input, 80)

def part2(input):
    return calc(input, 256)

def main():
    with open("day06/input.txt") as f:
        input = f.read()
        print(f"solution for part 1 is: {part1(input)}")
        print(f"solution for part 2 is: {part2(input)}")

if __name__ == "__main__":
    main()