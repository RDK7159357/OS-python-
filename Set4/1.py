# 10. Managing System and User Processes
def manage_processes(system_processes, user_processes):
    print("System Processes:")
    for process in system_processes:
        print(f"System Process: {process['id']} - Priority: {process['priority']}")

    print("\nUser Processes:")
    for process in user_processes:
        print(f"User Process: {process['id']} - Priority: {process['priority']}")

system_procs = [{'id': 101, 'priority': 1}, {'id': 102, 'priority': 2}]
user_procs = [{'id': 201, 'priority': 3}, {'id': 202, 'priority': 4}]
manage_processes(system_procs, user_procs)