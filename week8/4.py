def cscan_disk_scheduling(initial_head, requests, max_track=9999):
    total_head_movement = 0
    current_position = initial_head
    tracks_visited = []

    # Separate requests into those below and above the current head position
    requests_below = sorted([r for r in requests if r < current_position])
    requests_above = sorted([r for r in requests if r >= current_position])

    # First, service requests going up
    for request in requests_above:
        total_head_movement += abs(current_position - request)
        current_position = request
        tracks_visited.append(request)

    # After reaching the end, move to the maximum track if not already there
    if current_position < max_track:
        total_head_movement += abs(current_position - max_track)
        current_position = max_track

    # Move from max track to 0 to simulate circular behavior
    total_head_movement += abs(current_position - 0)
    current_position = 0

    # Continue servicing requests from the start of the disk
    for request in requests_below:
        total_head_movement += abs(current_position - request)
        current_position = request
        tracks_visited.append(request)

    return total_head_movement, tracks_visited

# Driver Code
initial_head_position = 4000
disk_requests = [4200, 1000, 6000, 7500, 2000]
total_head_movement, tracks_visited = cscan_disk_scheduling(initial_head_position, disk_requests)
print("Total Head Movement:", total_head_movement)
print("Order of Tracks Visited:", tracks_visited)
