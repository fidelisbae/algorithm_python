N = int(input())
count = 0

if N <= 1:
    primes = []
else:
    is_prime_list = [True] * (N + 1)
    is_prime_list[0] = is_prime_list[1] = False

    for i in range(2, int(N**0.5) + 1):
        if is_prime_list[i]:
            for j in range(i * i, N + 1, i):
                is_prime_list[j] = False

    primes = [i for i in range(2, N + 1) if is_prime_list[i]]

left = 0
right = 0
total = 0

while right < len(primes):
    total = total + primes[right]

    while total > N and left <= right:
        total = total - primes[left]
        left = left + 1

    if total == N:
        count = count + 1

    right = right + 1

print(count)
