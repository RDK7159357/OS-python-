# def calculate_total_time(orders, time_quantum): 
#   total_time=0
#   while any(orders):
#     for i in range(len(orders)):
#         if orders[i]>0:
#           if orders[i]<=time_quantum:
#             total_time+=orders[i]
#             orders[i]=0
#           else:
#             total_time+=time_quantum
#             orders[i]-=time_quantum
# # Write code here     
#   return total_time 
from collections import deque

def calculate_total_time(orders, time_quantum):
    orders_deque = deque(orders)
    total_time = 0

    while orders_deque:
        order = orders_deque[0]
        if order <= time_quantum:
            total_time += order
            orders_deque.popleft()
        else:
            total_time += time_quantum
            orders_deque[0] -= time_quantum

    return total_time

# Driver Code
orders = [5, 3, 8, 6]
time_quantum = 4
total_time = calculate_total_time(orders, time_quantum)
print(f"The total time required to complete all orders is: {total_time} minutes")
# Driver Code 
orders = [5, 3, 8, 6] 
time_quantum = 4 
total_time = calculate_total_time(orders, time_quantum) 
print(f"The total time required to complete all orders is: {total_time} minutes") 