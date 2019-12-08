def read_input():
    with open("input.txt", "r") as filestream:
        parents = {}
        for line in filestream:
            parent, child = line.strip().split(')')
            parents[child] = parent
    return parents

if __name__ == "__main__":
    parents = read_input()
    sum = 0
    for parent in parents:
        while parent in parents:
            parent = parents[parent]
            sum += 1

    print(sum)
        

