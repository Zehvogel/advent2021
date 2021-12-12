import time

def prepare_graph(input):
    adjacencies = {}
    lines = (l.strip() for l in input)
    for l in lines:
        a, b = l.split("-")
        if a in adjacencies.keys():
            adjacencies[a].append(b)
        else:
            adjacencies[a] = [b]
        if b in adjacencies.keys():
            adjacencies[b].append(a)
        else:
            adjacencies[b] = [a]
    return adjacencies

def visit(node, visited, adj, twice):
    paths = []
    visited.append(node)
    if node == "end":
        paths.append(visited)
    else:
        for n in adj[node]:
            if n.islower() and n in visited:
                if n != "start" and not twice:
                    paths += visit(n, visited.copy(), adj, True)
                else:
                    continue
            else:
                paths += visit(n, visited.copy(), adj, twice)
    return paths


def part1(input):
    adj = prepare_graph(input)
    paths = visit("start", [], adj, True)
    return len(paths)

def part2(input):
    adj = prepare_graph(input)
    paths = visit("start", [], adj, False)
    return len(paths)

def main():
    with open("day12/input.txt") as f:
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