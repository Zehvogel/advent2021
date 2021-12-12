import time
from statistics import median


def process_linec(line):
    ob = ["(", "[", "{", "<"]
    s = []
    for c in line:
        if c in ob:
            s.append(c)
        elif c == ")" and s.pop() != "(":
            return c
        elif c == "]" and s.pop() != "[":
            return c
        elif c == "}" and s.pop() != "{":
            return c
        elif c == ">" and s.pop() != "<":
            return c
    return "x"

def part1(input):
    score = {")": 3, "]": 57, "}": 1197, ">": 25137, "x": 0}
    res = 0
    lines = (l.strip() for l in input)
    for line in lines:
        c = process_linec(line)
        res += score[c]
    return res

def process_linei(line):
    s = []
    ob ={"(": 1, "[": 2, "{": 3, "<": 4}
    for c in line:
        if c in ob.keys():
            s.append(c)
        else:
            s.pop()
    res = 0
    for b in reversed(s):
        res = 5 * res + ob[b]
    return res


def part2(input):
    res = []
    lines = (l.strip() for l in input)
    for line in lines:
        if process_linec(line) != "x":
            continue
        res.append(process_linei(line))
    return median(res)


def main():
    with open("day10/input.txt") as f:
        input = f.readlines()
        t0 = time.perf_counter_ns()
        print(f"solution for part 1 is: {part1(input)}")
        t1 = time.perf_counter_ns()
        print(f"part 1 took {t1-t0} ns")
        print(f"solution for part 2 is: {part2(input)}")
        t2 = time.perf_counter_ns()
        print(f"part 2 took {t2-t1} ns")


if __name__ == "__main__":
    main()
