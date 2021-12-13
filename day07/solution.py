def cost_f1(a, b):
    return abs(a-b)

def cost_f2(a, b):
    n = abs(a-b)
    return n * (n + 1) // 2

def calc_cost_x(input, cost_f, x):
    cost = 0
    for i in input:
        cost += cost_f(i, x)
    return cost

def calc_cost(input, cost_f):
    x_min = min(input)
    x_max = max(input)
    cost_min = calc_cost_x(input, cost_f, x_max)
    x_cost_min = x_max
    for x in range(x_min, x_max):
        c = calc_cost_x(input, cost_f, x)
        if c < cost_min:
            cost_min = c
            x_cost_min = x

    return (x_cost_min, cost_min)

def part1(input):
    return calc_cost(input, cost_f1)

def part2(input):
    return calc_cost(input, cost_f2)

def main():
    with open("day07/input.txt") as f:
        input = [int(x) for x in f.read().split(",")]
        print(f"solution for part 1 is: {part1(input)}")
        print(f"solution for part 2 is: {part2(input)}")

if __name__ == "__main__":
    main()