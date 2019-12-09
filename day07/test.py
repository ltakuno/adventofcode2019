from itertools import permutations


configs  = permutations(range(5))
cont = 0
for c in configs:
    cont += 1
    for i in range(len(c)):
        print(c[i], end = '')
    print()

print('tamanho: %d' % (cont))

