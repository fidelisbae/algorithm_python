first_line = input()
goal = int(first_line.split()[0])
number_of_cities = int(first_line.split()[1])

advertisements = []

for i in range(number_of_cities):
    line = input()
    advertisement = {}
    advertisement["cost"] = int(line.split()[0])
    advertisement["customer"] = int(line.split()[1])
    advertisements.append(advertisement)


MAX_CUSTOMER = goal + 100
INF = float("inf")
dp = [INF] * (MAX_CUSTOMER + 1)

dp[0] = 0

for i in range(len(advertisements)):
    customer = advertisements[i]["customer"]
    cost = advertisements[i]["cost"]
    for j in range(customer, MAX_CUSTOMER + 1):
        dp[j] = min(dp[j], dp[j - customer] + cost)

print(min(dp[goal:]))
