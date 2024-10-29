import threading
import time

# Resources available in the system
resources = {
    'computers': ['R1', 'R2', 'R3'],
    'projectors': ['P1', 'P2']
}

# Team requests for specific resources
team_requests = {
    'TeamA': {'computer': 'R1', 'projector': 'P1'},
    'TeamB': {'computer': 'R2', 'projector': 'P2'},
    'TeamC': {'computer': 'R3', 'projector': 'P2'}
}

# Track allocated resources for each team
allocated_resources = {
    'TeamA': {'computer': None, 'projector': None},
    'TeamB': {'computer': None, 'projector': None},
    'TeamC': {'computer': None, 'projector': None}
}

# Locks to control access to resources
resource_locks = {
    'computers': {res: threading.Lock() for res in resources['computers']},
    'projectors': {res: threading.Lock() for res in resources['projectors']}
}


def request_resource(team, resource_type, resource):
    """Request a resource for a team."""
    lock = resource_locks[resource_type][resource]
    acquired = lock.acquire(timeout=1)  # Try acquiring the resource with a timeout

    if acquired:
        allocated_resources[team][resource_type] = resource
        print(f"{team} acquired {resource_type} {resource}")
        return True
    else:
        print(f"{team} failed to acquire {resource_type} {resource}")
        return False


def release_resource(team, resource_type, resource):
    """Release a resource held by a team."""
    if resource is not None:
        resource_locks[resource_type][resource].release()
        allocated_resources[team][resource_type] = None
        print(f"{team} released {resource_type} {resource}")


def team_work(team):
    """Simulate the work of a team by acquiring and releasing resources."""
    # Get the resources requested by the team
    computer = team_requests[team]['computer']
    projector = team_requests[team]['projector']

    # Try to acquire both resources
    computer_acquired = request_resource(team, 'computers', computer)
    projector_acquired = request_resource(team, 'projectors', projector)

    if computer_acquired and projector_acquired:
        # Simulate work by sleeping
        print(f"{team} is working with {computer} and {projector}...")
        time.sleep(2)

        # Release the resources after work is done
        release_resource(team, 'computers', computer)
        release_resource(team, 'projectors', projector)
    else:
        # If any resource was not acquired, release the one that was acquired
        if computer_acquired:
            release_resource(team, 'computers', computer)
        if projector_acquired:
            release_resource(team, 'projectors', projector)

    print(f"{team} finished work.")


# Create and start threads for each team
threads = []
for team in team_requests.keys():
    thread = threading.Thread(target=team_work, args=(team,))
    threads.append(thread)
    thread.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()

print("Simulation complete.")
