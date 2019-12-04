def valid_password(n):
    d1 = n % 10
    n = n // 10
    ok = False
    cont_digits = 1
    while (n):
        d2 = n % 10
        if (d1 < d2):
            return False
        if (d1 == d2):
            cont_digits = cont_digits + 1
        else:
            if (cont_digits == 2):
                ok = True
            cont_digits = 1
        d1 = d2
        n = n // 10
    if (cont_digits == 2):
        ok = True
    return ok


print('teste 112233', valid_password(112233))
print('teste 123444', valid_password(123444))
print('teste 111122', valid_password(111122))
print('teste 112223', valid_password(112223))




n = 124075
cont = 0
while (n <= 580769):
    if valid_password(n):
        cont = cont + 1
    n = n + 1

print('Total of different passwords within range meet these criteria %d' % (cont))
