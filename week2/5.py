from queue import Queue 
def calculate_total_time(high_priority_jobs, medium_priority_jobs, 
low_priority_jobs): 
  hq=Queue()
  mq=Queue()
  lq=Queue()
  total_time=0
  for job in high_priority_jobs.values():
    hq.put(job)
  for job in low_priority_jobs.values():
    lq.put(job)
  for job in medium_priority_jobs.values():
    mq.put(job)
  while not hq.empty():
    total_time+=hq.get()
  while not mq.empty():
    total_time+=mq.get()
  while not lq.empty():
    total_time+=lq.get()
  
# Write code here  
  return total_time 
# Driver Code 
high_priority_jobs = {'Job A': 20, 'Job B': 15, 'Job C': 25,} 
medium_priority_jobs = {'Job D': 10, 'Job E': 12, 'Job F': 8,} 
low_priority_jobs = {'Job G': 5, 'Job H': 4, 'Job I': 6,} 
total_time = calculate_total_time(high_priority_jobs, medium_priority_jobs, 
low_priority_jobs) 
print(f"The total time required to complete all jobs is: {total_time} units") 