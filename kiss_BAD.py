def sum(n, first=0):
    if n == first:
        return 0
    else:
        return n + sum(n-1, (n+first)//2) + sum((n+first)//2, first)
