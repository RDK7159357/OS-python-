def fcfs_disk_scheduling(initial_head, requests):
    # Initialize variables
    total_head_movement = 0
    current_position = initial_head
    tracks_visited = []

    # Process each request in the order it appears
    for request in requests:
        # Calculate the distance from the current position to the request
        movement = abs(current_position - request)
        total_head_movement += movement
        # Move the head to the requested position
        current_position = request
        # Track the order of tracks visited
        tracks_visited.append(request)

    return total_head_movement, tracks_visited

# Driver Code
initial_head_position = 150
disk_requests = [200, 50, 800, 300, 100]
total_head_movement, tracks_visited = fcfs_disk_scheduling(initial_head_position, disk_requests)
print("Total Head Movement:", total_head_movement)
print("Order of Tracks Visited:", tracks_visited)
