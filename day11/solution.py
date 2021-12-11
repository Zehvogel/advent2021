import time
import numpy as np

def incnflash(i, j, m, flashes):
    m[i, j] += 1
    if m[i, j] > 9 and not flashes[i, j]:
        flashes[i, j] = True
        flash(i, j, m, flashes)


def flash(i, j, m, flashes):
    up = i > 0
    left = j > 0
    down = i < m.shape[0] - 1
    right = j < m.shape[1] - 1
    if up:
        incnflash(i-1, j, m, flashes)
        if left:
            incnflash(i-1, j-1, m, flashes)
        if right:
            incnflash(i-1, j+1, m, flashes)
    if down:
        incnflash(i+1, j, m, flashes)
        if left:
            incnflash(i+1, j-1, m, flashes)
        if right:
            incnflash(i+1, j+1, m, flashes)
    if left:
        incnflash(i, j-1, m, flashes)
    if right:
        incnflash(i, j+1, m, flashes)

def do_step(m):
    m += 1
    flashes = m > 9
    for i, j in np.argwhere(flashes):
        flash(i, j, m, flashes)
    m[flashes] = 0
    return np.sum(flashes)

def calc_steps(m, steps):
    res = 0
    for i in range(steps):
        res += do_step(m)
    return res

def calc_steps2(m):
    res = 0
    flashes = 0
    while flashes < m.size:
        flashes = do_step(m)
        res += 1
    return res

def part1(input):
    m = np.asarray([[int(x) for x in line.strip()] for line in input])
    return calc_steps(m, 100)

def part2(input):
    m = np.asarray([[int(x) for x in line.strip()] for line in input])
    return calc_steps2(m)

def main():
    with open("day11/input.txt") as f:
        input =  f.readlines()
        t0 = time.perf_counter_ns()
        print(f"solution for part 1 is: {part1(input)}")
        t1 = time.perf_counter_ns()
        print(f"part 1 took {t1-t0} ns")
        print(f"solution for part 2 is: {part2(input)}")
        t2 = time.perf_counter_ns()
        print(f"part 2 took {t2-t1} ns")

if __name__ == "__main__":
    main()