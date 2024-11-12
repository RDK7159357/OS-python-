import threading
import time
import random

class ReservationSystem:
    def __init__(self, num_tables):
        # Initialize a dictionary to store table status (True if available, False if reserved)
        self.tables = {f'Table{i+1}': True for i in range(num_tables)}
        # Lock to manage concurrent access to tables
        self.lock = threading.Lock()

    def reserve_table(self, table_id):
        with self.lock:
            # Check if the table is available
            if self.tables.get(table_id, False):
                # Reserve the table if available
                self.tables[table_id] = False
                print(f"{table_id} reserved.")
                return True
            else:
                print(f"{table_id} is already reserved.")
                return False

    def release_table(self, table_id):
        with self.lock:
            # Release the table (mark it as available)
            if table_id in self.tables and not self.tables[table_id]:
                self.tables[table_id] = True
                print(f"{table_id} released.")
            else:
                print(f"{table_id} is not reserved or does not exist.")

def customer_request(reservation_system, table_id):
    # Attempt to reserve a table
    reserved = reservation_system.reserve_table(table_id)
    if reserved:
        # Simulate the customer using the table for some time
        time.sleep(random.uniform(0.5, 2.0))
        # Release the table after use
        reservation_system.release_table(table_id)

# Driver Code
reservation_system = ReservationSystem(num_tables=10)
threads = []
table_ids = [f'Table{i+1}' for i in range(10)]

for _ in range(20):  # Simulate 20 customer requests
    table_id = random.choice(table_ids)
    t = threading.Thread(target=customer_request, args=(reservation_system, table_id))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("All reservations completed.")
