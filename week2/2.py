from queue import Queue 
def calculate_total_time(high_priority_jobs, low_priority_jobs): 
  total_time=0
  hq=Queue()
  lq=Queue()
  for time in high_priority_jobs.values():
    hq.put(time)
  for time in low_priority_jobs.values():
    lq.put(time)
  while not hq.empty():
    total_time+=hq.get()
  while not lq.empty():
    total_time+=lq.get()
# Write code here  
  return total_time 
# Write code here  
high_priority_jobs = {'Job A': 8, 'Job B': 5, 'Job C': 10,} 
low_priority_jobs = {'Job D': 6, 'Job E': 3, 'Job F': 7,} 
total_time = calculate_total_time(high_priority_jobs, low_priority_jobs) 
print(f"The total time required to complete all jobs is: {total_time} units")