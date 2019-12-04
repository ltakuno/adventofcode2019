import sys

def distance_manhatan(p1, p2):
	return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def read_file():
	routes = []
	with open('input.txt', 'r') as filestream:
		for line in filestream:
			routes.append(line.split(","))
	return routes

def get_positions(route):
        up    = 0
        down  = 1
        left  = 2
        right = 3
	dir = [-1,+1,-1,+1]
	x = 0
	y = 0
	pos = []
        for d in route:
		nn = int(d[1:])
		if d[0] == 'U':
			while (nn > 0):
				y = y + dir[up]
				pos.append((x, y))
				nn = nn - 1
		if d[0] == 'D':
			while (nn > 0):
				y = y + dir[down]
				pos.append((x,y))
				nn = nn - 1

		if d[0] == 'L':
			while (nn > 0):
				x = x + dir[left]
				pos.append((x, y))
				nn = nn - 1

		if d[0] == 'R':
			while (nn > 0):
				x = x + dir[right]
				pos.append((x, y))
				nn = nn - 1
	return pos


if __name__ == '__main__':
        routes = read_file()

        pos0 = get_positions(routes[0])
        pos1 = get_positions(routes[1])

        hash = {}

        step0 = 0

        for p0 in pos0:
            step0 = step0 + 1
            hash[p0] = step0


        origin = (0, 0)
        step1 = 0
        minor = sys.maxint
        minor_step = sys.maxint

        for p1 in pos1:
            step1 = step1 + 1
            if hash.get(p1) is not None:
                if (hash.get(p1) + step1 < minor_step):
                    minor_step = hash.get(p1) + step1
                    print(minor_step)

                distance = distance_manhatan(origin, p1)
                if (distance < minor):
                        minor = distance
                        print(minor)

        print('Menor numero de passos: ')
        print(minor_step)


        print('Menor: ')
        print(minor)
	
