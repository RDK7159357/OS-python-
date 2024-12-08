# 6. Deadlock Prevention using Banker's Algorithm
def bankers_algorithm(available, max_demand, allocation):
    n = len(allocation)
    need = [[max_demand[i][j] - allocation[i][j] for j in range(len(available))] for i in range(n)]
    finish = [False] * n
    safe_sequence = []

    while len(safe_sequence) < n:
        found = False
        for i in range(n):
            if not finish[i] and all(need[i][j] <= available[j] for j in range(len(available))):
                safe_sequence.append(i)
                available = [available[j] + allocation[i][j] for j in range(len(available))]
                finish[i] = True
                found = True
                break
        if not found:
            print("System is in unsafe state!")
            return

    print(f"Safe sequence: {safe_sequence}")

available_resources = [3, 3, 2]
max_demand_matrix = [[7, 5, 3], [3, 2, 2], [9, 0, 2], [2, 2, 2], [4, 3, 3]]
allocation_matrix = [[0, 1, 0], [2, 0, 0], [3, 0, 2], [2, 1, 1], [0, 0, 2]]
bankers_algorithm(available_resources, max_demand_matrix, allocation_matrix)
