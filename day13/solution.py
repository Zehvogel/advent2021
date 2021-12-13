import time
import numpy as np
import matplotlib.pyplot as plt


def fold(vals, folds):
    new_vals = set()
    a, x = folds
    for v in vals:
        if a == "x":
            if v[0] < x:
                new_vals.add(v)
            else:
                new_vals.add((2*x -v[0], v[1]))
        elif a == "y":
            if v[1] < x:
                new_vals.add(v)
            else:
                new_vals.add((v[0], 2*x -v[1]))
    return new_vals
        
def prepare(input):
    vals, folds = input.split("\n\n")
    vals = [tuple([int(a) for a in v.split(",")]) for v in vals.split()]
    # very readable :)
    folds = [tuple([f.split(" ")[2].split("=")[0], int(f.split(" ")[2].split("=")[1])]) for f in folds.strip().split("\n")]
    return (set(vals), folds)

def part1(input):
    vals, folds = prepare(input)
    res = len(fold(vals, folds[0]))
    return res

def part2(input):
    vals, folds = prepare(input)
    for f in folds:
        vals = fold(vals, f)
    dims = [0, 0]
    for v in vals:
        for i, a in enumerate(v):
            if a > dims[i]:
                dims[i] = a
    dims[0] += 1
    dims[1] += 1
    res = np.zeros(tuple(dims))
    for v in vals:
        res[v] = 1
    plt.matshow(res.T)
    plt.show()
    return "look at the picture"

def main():
    with open("day13/input.txt") as f:
        input =  f.read()
        t0 = time.perf_counter_ns()
        print(f"solution for part 1 is: {part1(input)}")
        t1 = time.perf_counter_ns()
        print(f"part 1 took {t1-t0} ns")
        print(f"solution for part 2 is: {part2(input)}")
        t2 = time.perf_counter_ns()
        print(f"part 2 took {t2-t1} ns")

if __name__ == "__main__":
    main()