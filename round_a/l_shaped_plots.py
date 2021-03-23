'''
1. check_L
    # Rule 1:
    a. share the common endpoint
    b. both segment cannot have same length
    c. longer segment cannot be longer than shorter one
2.

'''

def check_L(graph):
    return

def build_graph(R,C):
    newlist = []
    for x in range(R):
        newlist.append(input().split())
    return newlist

for t in range(int(input())):
    R, C = input().split()
    graph = build_graph(int(R),int(C))
    # _dfs()
    print('Case #{}: {}'.format(t+1, graph))