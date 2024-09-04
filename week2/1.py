# from queue import Queue 
# def calculate_total_time(system_processes, user_processes): 
#   total_time=0
#   for k,v in system_processes.items():
#     total_time+=v
#   for k,v in user_processes.items():
#     total_time+=v

# # Write code here  
#   return total_time 
# # Driver Code 
# system_processes = {'Process A': 5,'Process B': 3,'Process C': 7,} 
# user_processes = {'Process D': 4, 'Process E': 2, 'Process F': 6,} 
# total_time = calculate_total_time (system_processes, user_processes) 
# print(f"The total time required to complete all processes is: {total_time} units") 
from queue import Queue

def calculate_total_time(system_processes, user_processes):
    system_queue = Queue()
    user_queue = Queue()

    # Add system processes to the system queue
    for time in system_processes.values():
        system_queue.put(time)

    # Add user processes to the user queue
    for time in user_processes.values():
        user_queue.put(time)

    total_time = 0

    # Process system processes
    while not system_queue.empty():
        total_time += system_queue.get()

    # Process user processes
    while not user_queue.empty():
        total_time += user_queue.get()

    return total_time

# Driver Code
system_processes = {'Process A': 5, 'Process B': 3, 'Process C': 7}
user_processes = {'Process D': 4, 'Process E': 2, 'Process F': 6}

total_time = calculate_total_time(system_processes, user_processes)
print(f"The total time required to complete all processes is: {total_time} units")