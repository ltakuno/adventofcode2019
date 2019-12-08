def find_path(origin):
    parents = read_input()
    path = []
    parent = parents[origin]

    while parent in parents:
        path.append(parent)
        parent = parents[parent]

    path.reverse()
    return path

def read_input():
    with open("input.txt", "r") as filestream:
        parents = {}
        for line in filestream:
            parent, child = line.strip().split(')')
            parents[child] = parent
    return parents

if __name__ == "__main__":

    p1 = find_path("YOU")
    p2 = find_path("SAN")

    i = 0

    while (p1[i] == p2[i]):
        i += 1

    answer = ((len(p1) - i) + (len(p2) - i))
    print(answer)

        

