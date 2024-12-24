# 13. Job Scheduling by Priority
def priority_scheduling(jobs):
    jobs.sort(key = lambda x:x['priority'])
    for i in jobs:
        print(f"Exec Job {i['id']} with priority {i['priority']}")
    
job_list = [{'id': 1, 'priority': 2}, {'id': 2, 'priority': 1}, {'id': 3, 'priority': 3}]
priority_scheduling(job_list)