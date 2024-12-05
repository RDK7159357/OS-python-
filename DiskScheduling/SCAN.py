def scan_disk_scheduling(initial_head, requests, direction='up', max_track=4999):
    total_head_movement = 0
    current_position = initial_head
    tracks_visited = []

    # Separate requests into those below and above the current head position
    requests_below = sorted([r for r in requests if r < current_position])
    requests_above = sorted([r for r in requests if r >= current_position])

    if direction == 'up':
        # First, serve requests going upwards
        for request in requests_above:
            total_head_movement += abs(current_position - request)
            current_position = request
            tracks_visited.append(request)
        
        # Reach the end of the disk, if necessary
        if current_position < max_track:
            total_head_movement += abs(current_position - max_track)
            current_position = max_track

        # Then, reverse direction and serve requests going downwards
        for request in reversed(requests_below):
            total_head_movement += abs(current_position - request)
            current_position = request
            tracks_visited.append(request)

    elif direction == 'down':
        # First, serve requests going downwards
        for request in reversed(requests_below):
            total_head_movement += abs(current_position - request)
            current_position = request
            tracks_visited.append(request)

        # Reach the start of the disk, if necessary
        if current_position > 0:
            total_head_movement += abs(current_position - 0)
            current_position = 0

        # Then, reverse direction and serve requests going upwards
        for request in requests_above:
            total_head_movement += abs(current_position - request)
            current_position = request
            tracks_visited.append(request)

    return total_head_movement, tracks_visited

# Driver Code
initial_head_position = 2500
disk_requests = [2800, 1500, 3500, 4000, 1000]
total_head_movement, tracks_visited = scan_disk_scheduling(initial_head_position, disk_requests, direction='up')
print("Total Head Movement:", total_head_movement)
print("Order of Tracks Visited:", tracks_visited)
