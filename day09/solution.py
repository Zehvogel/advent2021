import time
import numpy as np


def part1(input):
    res = 0
    m = np.asarray([[int(x) for x in line.strip()] for line in input])
    n_y = m.shape[0]
    n_x = m.shape[1]
    for j in range(n_y):
        for i in range(n_x):
            center = m[j, i]
            up = m[j-1, i] if j-1 >= 0 else 9
            down = m[j+1, i] if j+1 < n_y else 9
            left = m[j, i-1] if i-1 >= 0 else 9
            right = m[j, i+1] if i+1 < n_x else 9

            if center < up and center < down and center < left and center < right:
                res += center + 1

    return res

def update_basins(basins, neighbors, pos):
    n_basins = []
    for n in neighbors:
        for b in basins:
            if n in b:
                n_basins.append(b)
                basins.remove(b)
    new_basin = set(neighbors)
    new_basin.add(pos)
    for b in n_basins:
        new_basin |= b
    basins.append(new_basin)


def part2(input):
    res = 0
    m = np.asarray([[int(x) for x in line.strip()] for line in input])
    m = m < 9
    m = m*1
    mrange = np.ndindex(m.shape)
    n_y = m.shape[0]
    n_x = m.shape[1]
    basins = []
    for j in range(n_y):
        for i in range(n_x):
            if m[j, i] == 0:
                continue

            # neigbor in basin?
            neighbors = []
            upos = (j-1, i)
            if upos[0] >= 0 and m[upos] != 0:
                neighbors.append(upos)
            dpos = (j+1, i)
            if dpos[0] < n_y and m[dpos] != 0:
                neighbors.append(dpos)
            lpos = (j, i-1)
            if lpos[1] >= 0 and m[lpos] != 0:
                neighbors.append(lpos)
            rpos = (j, i+1)
            if rpos[1] < n_x and m[rpos] != 0:
                neighbors.append(rpos)

            update_basins(basins, neighbors, (j, i))

    sizes = np.sort([len(b) for b in basins])

    return sizes[-1] * sizes[-2] * sizes[-3]

def main():
    with open("day09/input.txt") as f:
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