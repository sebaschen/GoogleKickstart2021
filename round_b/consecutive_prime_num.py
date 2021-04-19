# 1. product of two  two consecutive prime numbers
# 2. largest number should be <= Z

prime_list = [x for x in range(2,10**18) if not [t for t in range(2,x) if not x%t]]

def get_concecutive_primes(max_number,prime_list):
    for i in range(len(prime_list)-2):
        product_of_two_primes = prime_list[i]*prime_list[i+1]
        if product_of_two_primes > max_number:
            z =  int(prime_list[i]*prime_list[i-1])
            print('Case #{}: {}'.format(t+1, z))
            break

for t in range(int(input())):
    max_number = int(input())
    get_concecutive_primes(max_number,prime_list)



