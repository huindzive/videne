def sum(n):
    if n == 0:
        return 0
    else:
        return n + sum(n-1)

print(sum(5))

def grid_paths(n,m):
    if n== 1 or m == 1:
        return 1
    else:
        return grid_paths(n, m-1) + grid_paths(n-1,m)

def partitions(n, m):
    if n == 0:
        return 1
    elif m == 0 or n < 0:
        return 0
    else:
        return partitions(n - m, m) + partitions(n, m-1)