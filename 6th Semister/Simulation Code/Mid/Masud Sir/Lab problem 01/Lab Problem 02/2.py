import random

# -------------------------
# Inventory Parameters
# -------------------------
days = 30
initial_stock = 50
mean_demand = 8
reorder_point = 15
order_quantity = 40
lead_time = 3

random.seed(1)

# -------------------------
# Variables
# -------------------------
stock = initial_stock
pipeline = []   # list of (arrival_day, quantity)

total_demand = 0
total_served = 0
total_lost = 0
stockout_days = 0
orders = 0
sum_stock = 0

# -------------------------
# Simulation Loop
# -------------------------
for day in range(1, days + 1):

    # Receive deliveries
    arrived = 0
    new_pipeline = []
    for (arrival_day, qty) in pipeline:
        if arrival_day == day:
            arrived += qty
        else:
            new_pipeline.append((arrival_day, qty))

    pipeline = new_pipeline
    stock += arrived

    # Generate random demand
    demand = max(0, int(random.gauss(mean_demand, 2)))
    total_demand += demand

    # Serve demand
    served = min(stock, demand)
    lost = demand - served
    stock -= served

    total_served += served
    total_lost += lost

    if lost > 0:
        stockout_days += 1

    # Check reorder condition
    on_order = sum(qty for _, qty in pipeline)
    inventory_position = stock + on_order

    if inventory_position <= reorder_point:
        arrival_day = day + lead_time
        pipeline.append((arrival_day, order_quantity))
        orders += 1

    sum_stock += stock

# -------------------------
# Results
# -------------------------
average_stock = sum_stock / days
fill_rate = total_served / total_demand if total_demand > 0 else 1

print("\n--- Inventory Simulation Results ---")
print("Days simulated:", days)
print("Total demand:", total_demand)
print("Total served:", total_served)
print("Total lost sales:", total_lost)
print("Fill rate:", round(fill_rate, 4))
print("Stockout days:", stockout_days)
print("Average stock:", round(average_stock, 2))
print("Total orders placed:", orders)