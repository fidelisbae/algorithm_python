import sys

input = sys.stdin.readline

first_input = input().split()
NUMBER_OF_HOUSE, NUMBER_OF_ROAD = int(first_input[0]), int(first_input[1])

roads = []
parent = [i for i in range(NUMBER_OF_HOUSE + 1)]
rank = [0] * (NUMBER_OF_HOUSE + 1)
costs = []

for _ in range(NUMBER_OF_ROAD):
    start, end, cost = map(int, input().split())
    roads.append((cost, start, end))

roads.sort()


def find_root(parent, item):
    if parent[item] != item:
        parent[item] = find_root(parent, parent[item])
    return parent[item]


def union(parent, rank, a, b):
    root_a = find_root(parent, a)
    root_b = find_root(parent, b)

    if root_a == root_b:
        return False

    if rank[root_a] < rank[root_b]:
        parent[root_a] = root_b
    elif rank[root_a] > rank[root_b]:
        parent[root_b] = root_a
    else:
        parent[root_b] = root_a
        rank[root_a] += 1

    return True


for cost, start, end in roads:
    if union(parent, rank, start, end):
        costs.append(cost)

print(sum(costs) - max(costs))
