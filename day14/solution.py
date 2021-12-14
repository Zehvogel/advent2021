import time
from more_itertools import pairwise
from collections import Counter

def parse_rules(input):
    rules = {}
    for line in input:
        k, v = line.strip().split(" -> ")
        rules[k] = v
    return rules

def do_step_slow(s, rules):
    res = s[0]
    for a, b in pairwise(s):
        res += rules[a+b]
        res += b
    return res

def solve_slow(steps, input):
    s = input[0].strip()
    rules = parse_rules(input[2:])
    for i in range(steps):
        s = do_step_slow(s, rules)
    C = Counter(s)
    counts = C.most_common()
    m = counts[0][1]
    l = counts[-1][1]
    return m - l

def do_step(rules, C, res):
    counts = Counter()
    for k in C.keys():
        m = rules[k]
        l = k[0] + m
        r = m + k[1]
        c = C[k]
        res[m] += c
        counts[l] += c
        counts[r] += c
    return (res, counts)

def solve(steps, input):
    s = input[0].strip()
    rules = parse_rules(input[2:])
    C = Counter()
    for a, b in pairwise(s):
        C[a+b] += 1
    res = Counter(s)
    for i in range(steps):
        res, C = do_step(rules, C, res)
    counts = res.most_common()
    m = counts[0][1]
    l = counts[-1][1]
    return m - l

def part1(input):
    return solve(10, input)

def part2(input):
    return solve(40, input)

def main():
    with open("day14/input.txt") as f:
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