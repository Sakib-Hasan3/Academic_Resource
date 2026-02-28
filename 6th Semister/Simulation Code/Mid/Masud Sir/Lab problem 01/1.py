import random
import math
from collections import deque

def exp_rv(mean: float) -> float:
    """
    Generate an exponential random variable with given mean.
    If U ~ Uniform(0,1), then X = -mean * ln(U)
    """
    u = random.random()
    return -mean * math.log(u)

def mm1_simulation(mean_interarrival: float, mean_service: float, max_customers: int, seed: int = 1):
    # ----------------------------
    # Step 1) Initialize
    # ----------------------------
    random.seed(seed)

    clock = 0.0  # simulation clock

    server_busy = False
    queue = deque()  # stores arrival times of customers waiting in queue

    # Event times
    next_arrival = clock + exp_rv(mean_interarrival)
    next_departure = float("inf")  # no departure scheduled initially

    # Statistics
    num_completed = 0
    total_delay_in_queue = 0.0

    area_num_in_queue = 0.0      # ∫ Q(t) dt
    area_server_busy = 0.0       # ∫ B(t) dt where B(t)=1 if busy else 0

    last_event_time = 0.0

    # ----------------------------
    # Step 2) Main event loop
    # ----------------------------
    while num_completed < max_customers:
        # Choose next event: arrival or departure
        if next_arrival < next_departure:
            event_time = next_arrival
            event_type = "ARRIVAL"
        else:
            event_time = next_departure
            event_type = "DEPARTURE"

        # ----------------------------
        # Step 3) Update time-average stats (areas)
        # ----------------------------
        time_since_last = event_time - last_event_time
        area_num_in_queue += len(queue) * time_since_last
        area_server_busy += (1.0 if server_busy else 0.0) * time_since_last

        # Advance clock
        clock = event_time
        last_event_time = clock

        # ----------------------------
        # Step 4) Process event
        # ----------------------------
        if event_type == "ARRIVAL":
            # Schedule next arrival
            next_arrival = clock + exp_rv(mean_interarrival)

            if not server_busy:
                # Server is idle -> customer starts service immediately (no queue delay)
                server_busy = True
                next_departure = clock + exp_rv(mean_service)
            else:
                # Server busy -> customer joins FIFO queue
                queue.append(clock)

        else:  # DEPARTURE
            num_completed += 1

            if len(queue) == 0:
                # No one waiting -> server becomes idle
                server_busy = False
                next_departure = float("inf")
            else:
                # Someone waiting -> take next customer from FIFO queue
                arrival_time = queue.popleft()
                delay = clock - arrival_time
                total_delay_in_queue += delay

                # Start service for this customer immediately
                next_departure = clock + exp_rv(mean_service)

    # ----------------------------
    # Step 5) Final metrics
    # ----------------------------
    sim_end_time = clock

    avg_delay_in_queue = total_delay_in_queue / max_customers
    avg_num_in_queue = area_num_in_queue / sim_end_time
    server_utilization = area_server_busy / sim_end_time

    return {
        "Average delay in queue (Wq)": avg_delay_in_queue,
        "Average number in queue (Lq)": avg_num_in_queue,
        "Server utilization (rho)": server_utilization,
        "Time simulation ended": sim_end_time,
    }

if __name__ == "__main__":
    # Example input
    mean_interarrival = float(input("Enter mean inter-arrival time: "))
    mean_service = float(input("Enter mean service time: "))
    max_customers = int(input("Enter max number of customers: "))

    results = mm1_simulation(mean_interarrival, mean_service, max_customers, seed=1)

    print("\n--- M/M/1 Simulation Results ---")
    for k, v in results.items():
        print(f"{k}: {v:.6f}")