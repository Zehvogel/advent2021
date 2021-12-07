def part1(input):
    pos = [0, 0]
    down = lambda pos, x: (pos[0], pos[1] + x)
    up = lambda pos, x: (pos[0], pos[1] - x)
    forward = lambda pos, x: (pos[0] + x, pos[1])
    move = {"forward": forward, "up": up, "down": down}
    for m, x in input:
        pos = move[m](pos, x)

    return pos[0] * pos[1]

def part2(input):
    pos = [0, 0, 0]
    down = lambda pos, x: (pos[0], pos[1], pos[2] + x)
    up = lambda pos, x: (pos[0], pos[1], pos[2] - x)
    forward = lambda pos, x: (pos[0] + x, pos[1] + pos[2] * x, pos[2])
    move = {"forward": forward, "up": up, "down": down}
    for m, x in input:
        pos = move[m](pos, x)

    return pos[0] * pos[1]

def main():
    with open("day2/input.txt") as f:
        f_split = (l.split(" ") for l in f)
        f_m = ((a, int(b)) for a, b in f_split)
        print(f"solution for part 1 is: {part1(f_m)}")
        f.seek(0)
        f_split = (l.split(" ") for l in f)
        f_m = ((a, int(b)) for a, b in f_split)
        print(f"solution for part 2 is: {part2(f_m)}")

if __name__ == "__main__":
    main()