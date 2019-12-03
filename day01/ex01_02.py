def require_fuel(mass):
    fuel = (mass // 3 - 2)
    if (fuel > 3):
        return  fuel + require_fuel(fuel)
    elif (fuel > 0):
        return fuel
    else:
        return 0


if __name__ == '__main__':
	total = 0
	while True:
		try:
			mass = int(input())
			total = total + require_fuel(mass)
		except EOFError:
			break
		
	print(total)