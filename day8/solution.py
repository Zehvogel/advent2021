import time


def get_lr(input):
    l, r = input.split("|")
    return (l.strip().split(), r.strip().split())

def part1(input):
    # digits = [1, 4, 7, 8]
    n_segments = [2, 4, 3, 7]
    count = 0
    for i in input:
        l, r = get_lr(i)
        for a in r:
            if len(a) in n_segments:
                count += 1
    return count

# :(
def first(a_set):
    for a in a_set:
        return a

def calc(r, char2id):
    res = ""
    #   0
    # 1   2
    #   3
    # 4   5
    #   6
    shape2num = {
        "[0, 1, 2, 4, 5, 6]": 0,
        "[2, 5]": 1,
        "[0, 2, 3, 4, 6]": 2,
        "[0, 2, 3, 5, 6]": 3,
        "[1, 2, 3, 5]": 4,
        "[0, 1, 3, 5, 6]": 5,
        "[0, 1, 3, 4, 5, 6]": 6,
        "[0, 2, 5]": 7,
        "[0, 1, 2, 3, 4, 5, 6]": 8,
        "[0, 1, 2, 3, 5, 6]": 9
    }
    for number in r:
        ids = set()
        for c in number:
            ids.add(char2id[c])
        res += str(shape2num[str(list(ids))])
    return int(res)

def process_line(line):
    len2num = {2: 1, 4: 4, 3: 7, 7: 8}
    l, r = get_lr(line)
    asc_dict = {}
    for a in l:
        k = len(a)
        if k in len2num.keys():
            asc_dict[len2num[k]] = set(a)

    for a in l:
        sa = set(a)
        #identify 9, 0, 6
        if len(a) == 6:
            if asc_dict[4] < sa:
                asc_dict[9] = sa
            elif asc_dict[1] < sa:
                asc_dict[0] = sa
            else:
                asc_dict[6] = sa

    for a in l:
        sa = set(a)
        #identify 2, 3, 5
        if len(a) == 5:
            if asc_dict[8] - asc_dict[9] < sa:
                asc_dict[2] = sa
            elif asc_dict[1] < sa:
                asc_dict[3] = sa
            else:
                asc_dict[5] = sa

    char2id = {}
    # find top segment by comparing 7 and 1
    c = first(asc_dict[7] - asc_dict[1])
    char2id[c] = 0

    c = first(asc_dict[8] - asc_dict[6])
    char2id[c] = 2

    c = first(asc_dict[8] - asc_dict[0])
    char2id[c] = 3

    c = first(asc_dict[8] - asc_dict[9])
    char2id[c] = 4

    diff = asc_dict[8] - asc_dict[2]
    for s in diff:
        if s in asc_dict[1]:
            char2id[s] = 5
        else:
            char2id[s] = 1

    for c in ["a", "b", "c", "d", "e", "f", "g"]:
        if c not in char2id.keys():
            char2id[c] = 6

    return calc(r, char2id)

def part2(input):
    res = 0
    for line in input:
        res += process_line(line)
    return res

def main():
    with open("day8/input.txt") as f:
        input =  f.readlines()
        print(f"solution for part 1 is: {part1(input)}")
        t0 = time.perf_counter_ns()
        print(f"solution for part 2 is: {part2(input)}")
        t1 = time.perf_counter_ns()
        print(f"part 2 took {t1-t0} ns")

if __name__ == "__main__":
    main()