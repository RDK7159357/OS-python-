def is_safe_state(processes, available, allocation, need):
    """Check if the system is in a safe state and return the safe sequence if it exists."""
    n = len(processes)  # Number of processes
    m = len(available)  # Number of resource types

    # Initialize a list to track which processes are finished
    finish = [False] * n
    safe_sequence = []

    # Create a copy of available resources to work with
    work = available[:]

    # Try to find a safe sequence
    while len(safe_sequence) < n:
        allocated_in_iteration = False

        for i in range(n):
            if not finish[i]:  # If process i is not finished
                # Check if the process's need can be satisfied with available resources
                if all(need[i][j] <= work[j] for j in range(m)):
                    # Allocate resources to the process (simulate execution)
                    for j in range(m):
                        work[j] += allocation[i][j]

                    # Mark the process as finished and add it to the safe sequence
                    finish[i] = True
                    safe_sequence.append(processes[i])
                    allocated_in_iteration = True
                    print(f"Process {processes[i]} has finished, resources released: {work}")
                    break  # Restart the search to look for other processes

        if not allocated_in_iteration:
            # No process could be allocated in this iteration, so the system is unsafe
            return False, []

    # If all processes are finished, the system is in a safe state
    return True, safe_sequence

# Driver Code
processes = ['P1', 'P2', 'P3', 'P4', 'P5']
available = [3, 2, 2]  # Available resources of each type
allocation = [
    [1, 2, 2],  # Resources allocated to P1
    [2, 0, 1],  # Resources allocated to P2
    [1, 1, 1],  # Resources allocated to P3
    [2, 1, 0],  # Resources allocated to P4
    [0, 0, 2]   # Resources allocated to P5
]
maximum = [
    [1, 2, 2],  # Maximum resources required by P1
    [2, 0, 1],  # Maximum resources required by P2
    [1, 1, 1],  # Maximum resources required by P3
    [2, 1, 0],  # Maximum resources required by P4
    [0, 0, 2]   # Maximum resources required by P5
]

# Calculate the need matrix
need = [[maximum[i][j] - allocation[i][j] for j in range(len(available))] 
        for i in range(len(processes))]

# Check if the system is in a safe state
is_safe, safe_sequence = is_safe_state(processes, available, allocation, need)

if is_safe:
    print("The system is in a safe state.")
    print("Safe sequence:", ' -> '.join(safe_sequence))
else:
    print("The system is in an unsafe state. Deadlock may occur.")
