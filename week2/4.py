from queue import Queue 
def calculate_total_time(high_priority_tasks, low_priority_tasks): 
  hq=Queue()
  lq=Queue()
  total_time=0
  for task in high_priority_tasks.values():
    hq.put(task)
  for task in low_priority_tasks.values():
    lq.put(task)
  while not hq.empty():
    total_time+=hq.get()
  while not lq.empty():
    total_time+=lq.get()
  
# Write code here  
  return total_time 
# Driver Code 
high_priority_tasks = {'Task A': 12, 'Task B': 8, 'Task C': 15,} 
low_priority_tasks = {'Task D': 6, 'Task E': 4, 'Task F': 10, } 
total_time = calculate_total_time(high_priority_tasks, low_priority_tasks) 
print(f"The total time required to complete all tasks is: {total_time} units") 