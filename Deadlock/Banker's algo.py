def bankers_algorithm(total, allocated, maximum):
    available = [total[i] - sum(a[i] for a in allocated) for i in range(len(total))]
    need = [[maximum[i][j] - allocated[i][j] for j in range(len(total))] for i in range(len(allocated))]
    finish = [False] * len(allocated)
    safe_sequence = []

    while len(safe_sequence) < len(allocated):
        allocated_in_round = False
        for i in range(len(allocated)):
            if not finish[i] and all(need[i][j] <= available[j] for j in range(len(total))):
                available = [available[j] + allocated[i][j] for j in range(len(total))]
                safe_sequence.append(i)
                finish[i] = True
                allocated_in_round = True
                break
        if not allocated_in_round:
            break

    if len(safe_sequence) == len(allocated):
        print(f"Safe state. Safe sequence: {safe_sequence}")
    else:
        print("Unsafe state. Deadlock possible.")

# Example usage
if __name__ == "__main__":
    total_resources = [10, 5, 7]
    allocated = [
        [0, 1, 0],
        [2, 0, 0],
        [3, 0, 2],
        [2, 1, 1],
        [0, 0, 2]
    ]
    maximum = [
        [7, 5, 3],
        [3, 2, 2],
        [9, 0, 2],
        [4, 2, 2],
        [5, 3, 3]
    ]
    bankers_algorithm(total_resources, allocated, maximum)
