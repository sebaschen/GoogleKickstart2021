def one_to_here(i, result, G):
    n = i
    result = 0
    while sum(range(i, n+1)) <= G:
        if sum(range(i, n+1)) == G:
            result += 1
            break
        n += 1
    return result


def combinations(G):
    result = 0
    i = 1
    for i in range(1, G):
        result += one_to_here(i, result, G)
        i += 1
    return result


for t in range(int(input())):
    G = int(input())
    z = combinations(G)
    print('Case #{}: {}'.format(t+1, z+1))
