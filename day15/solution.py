import time
from queue import PriorityQueue
import numpy as np


def neighbors(pos, shape):
    if pos[0] > 0:
        yield (pos[0] - 1, pos[1])
    if pos[1] > 0:
        yield (pos[0], pos[1] - 1)
    if pos[1] + 1 < shape[1]:
        yield (pos[0], pos[1] + 1)
    if pos[0] + 1 < shape[0]:
        yield (pos[0] + 1, pos[1])


def dijkstra(m, start):
    dist = np.full_like(m, np.inf, dtype=np.float64)
    dist[start] = 0

    q = PriorityQueue()
    q.put((0, start))

    while not q.empty():
        u = q.get()[1]
        d = dist[u]
        for v in neighbors(u, m.shape):
            new_dist = d + m[v]
            if new_dist < dist[v]:
                dist[v] = new_dist
                q.put((new_dist, v))
    return dist


def shortest_path(m, start, finish):
    td0 = time.perf_counter_ns()
    dist = dijkstra(m, start)
    td1 = time.perf_counter_ns()
    print(f"time for dijkstra: {td1- td0} ns")
    return dist[finish]

def part1(input):
    m = np.asarray([[int(x) for x in line.strip()] for line in input])
    n = m.shape[0] - 1
    dist = shortest_path(m, (0,0), (n, n))
    return dist

def inc(m):
    m += 1
    m[m > 9] = 1
    return m

def part2(input):
    ta0 = time.perf_counter_ns()
    m = np.asarray([[int(x) for x in line.strip()] for line in input])
    oldm = m.copy()
    for i in range(4):
        m = np.append(m, inc(oldm), 0)
    oldm = m.copy()
    for i in range(4):
        m = np.append(m, inc(oldm), 1)
    ta1 = time.perf_counter_ns()
    print(f"time for matrix init: {ta1 - ta0} ns")
    n = m.shape[0] - 1
    dist = shortest_path(m, (0,0), (n, n))
    return dist

def main():
    with open("day15/input.txt") as f:
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