def sstf_disk_scheduling(initial_head, requests):
    total_head_movement = 0
    current_position = initial_head
    tracks_visited = []

    while requests:
        # Find the closest request to the current position
        closest_request = min(requests, key=lambda x: abs(current_position - x))
        # Update total head movement
        total_head_movement += abs(current_position - closest_request)
        # Move to the closest request
        current_position = closest_request
        # Record the visit
        tracks_visited.append(closest_request)
        # Remove the closest request from the list
        requests.remove(closest_request)

    return total_head_movement, tracks_visited

# Driver Code
initial_head_position = 750
disk_requests = [1200, 500, 900, 1500, 300]
total_head_movement, tracks_visited = sstf_disk_scheduling(initial_head_position, disk_requests)
print("Total Head Movement:", total_head_movement)
print("Order of Tracks Visited:", tracks_visited)
