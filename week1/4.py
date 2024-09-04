# def calculate_total_time(patients): 
#   total_time=0
#   patients.sort(key=lambda x:x[0])
#   for patient in patients:
#     total_time+=patient[1]
# # Write code here 
#   return total_time 
# # Drive Code 
# patients = [(1, 10),  # Patient A: Priority 1, Treatment time 10 minutes 
# (2, 8),   # Patient B: Priority 2, Treatment time 8 minutes 
# (3, 15),  # Patient C: Priority 3, Treatment time 15 minutes 
# (4, 5)    
# # Patient D: Priority 4, Treatment time 5 minutes 
# ] 
# total_time = calculate_total_time(patients) 
# print(f"The total time required to treat all patients is: {total_time} minutes")  
from collections import deque

def calculate_total_time(patients):
    patients_deque = deque(sorted(patients, key=lambda x: x[0]))
    total_time = 0

    while patients_deque:
        patient = patients_deque.popleft()
        total_time += patient[1]

    return total_time

# Driver Code
patients = [(1, 10),  # Patient A: Priority 1, Treatment time 10 minutes
            (2, 8),   # Patient B: Priority 2, Treatment time 8 minutes
            (3, 15),  # Patient C: Priority 3, Treatment time 15 minutes
            (4, 5)    # Patient D: Priority 4, Treatment time 5 minutes
            ]

total_time = calculate_total_time(patients)
print(f"The total time required to treat all patients is: {total_time} minutes")