def gen(n):
    ''' Generate n number of fibonacci numbers '''
    n = int(n)
    a, b, c = 1, 1, 0
    while c < n:
        yield a
        a, b, c = b, a+b, c+1
