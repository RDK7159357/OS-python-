# 7. Managing Restaurant Orders using Round Robin
def round_robin(orders, time_quantum):
    time = 0
    while orders:
        order = orders.pop(0)
        if order['time'] > time_quantum:
            print(f"Processing Order {order['id']} for {time_quantum}s at t={time}s")
            order['time'] -= time_quantum
            orders.append(order)
            time += time_quantum
        else:
            print(f"Completing Order {order['id']} at t={time}s")
            time += order['time']

restaurant_orders = [{'id': 1, 'time': 10}, {'id': 2, 'time': 5}, {'id': 3, 'time': 8}]
round_robin(restaurant_orders, 4)