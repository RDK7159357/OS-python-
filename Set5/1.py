# 13. Job Scheduling by Priority
def priority_scheduling(jobs):
    for job in sorted(jobs, key=lambda x: x['priority']):
        print(f"Executing Job {job['id']} with priority {job['priority']}")

job_list = [{'id': 1, 'priority': 2}, {'id': 2, 'priority': 1}, {'id': 3, 'priority': 3}]
priority_scheduling(job_list)