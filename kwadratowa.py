def kwadratowa(a, b, c):
    if a == 0:
        if b == 0:
            return None, None
        else:
            x=-c/b
            return x, None
    else:
        x1= (-b - (b ** 2 - (4 * a * c))**0.5)/(2*a)
        x2= (-b + (b ** 2 - (4 * a * c))**0.5)/(2*a)
        return x1, x2


x1, x2 = kwadratowa(0, 2, 3)
print (x1,x2)
x1, x2 = kwadratowa(-1, 2, 3)
print (x1,x2)
x1, x2 = kwadratowa(2, 5, 3)
print (x1,x2)
x1, x2 = kwadratowa(0, 0, 1)
print (x1,x2)