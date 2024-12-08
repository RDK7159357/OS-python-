# 15. Disk Scheduling using SSTF Algorithm
def sstf(requests, head):
    sequence = []
    while requests:
        closest_request = min(requests, key=lambda x: abs(x - head))
        sequence.append(closest_request)
        requests.remove(closest_request)
        head = closest_request

    print("Seek Sequence:", sequence)

requests = [82, 170, 43, 140, 24, 16, 190]
initial_head = 50
sstf(requests, initial_head)