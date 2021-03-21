# ans: minimim_operation

def get_goodness_score(S,N):
    result = 0
    for i in range(N//2):
        if S[i] != S[N-i-1]:
            result +=1
    return result

for t in range(int(input())):
    N, K = input().split()
    S = str(input())
    N = int(N)
    K = int(K)
    goodness_score = get_goodness_score(S,N)
    minimum_operations = abs(K - goodness_score)

    print('Case #{}: {}'.format(t+1, minimum_operations))

