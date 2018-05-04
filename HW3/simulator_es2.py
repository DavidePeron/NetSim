import numpy as np

def get_service_time(b):
    u = np.random.rand()
    return int(np.log(u)/np.log(1-b)) + 1

def check_arrival_in_next_slot(a):
    coin = np.random.rand()
    #Check for arrival
    if(coin < a):
            return True
    return False

# Return a list with:
# - (int) distance from the next useful slot
# - (Bool) departure if True
# - (Bool)  arrival if True
def next_event(a, queue, server):
    event = [1, False, False]

    # Check for imminent departure
    if server['busy']:
        if server['counter'] == 1:
            event[2] = check_arrival_in_next_slot(a)
            event[1] = True
        else:
            i = server['counter'] - 1
            while i >= 1:
                if(check_arrival_in_next_slot(a)):
                    event[2] = True
                    event[0] = server['counter'] - i + 1
                    if i == 1:
                        event[1] = True
                    return event
                i -= 1
            event[0] = server['counter']
            event[1] = True
    else: # Check if the server is idle
        arrival = False
        while(not check_arrival_in_next_slot(a)):
            event[0] += 1
        event[2] = True
    return event

#slots_counter : number of iteration of the simulation
# 1/b : mean of the service time (geometric)
# a : arrival's probability
def run_queue(slots_counter, b = 0.2, a = 0.5, limited_size = False, maximum_size = 3):

    # print('Max size: '+ str(maximum_size))
    # print('Limited Queue: ' + str(limited_size))
    #Metrics
    queue_size = [0]
    delay = []
    busy_slots = 0
    num_arrivals = 0
    discarded_pkts = 0

    queue = []
    server = {'busy': False, 'counter': 0}

    while(slots_counter > 0):

        # Generate next event
        event = next_event(a, queue, server)

        # Update packet's delay
        queue = [pkt+event[0] for pkt in queue]

        # Insert a packet (an int starting from 1 that increase at each iteration
        # and indicates the number of slots that they remain in the queue)
        if event[2]:
            num_arrivals += 1
            # Check if the queue has a limited size and in that case if is at its max dimension
            if not limited_size or (limited_size and len(queue) < maximum_size):
                queue.insert(0,0)
            else:
                discarded_pkts += 1

        # Update departures
        if event[1]:
            server['busy'] = False
            server['counter'] = 0
        elif server['busy']:
            server['counter'] -= event[0]

        # If the queue is not empty, serve the last element and update server's counter
        if queue and not server['busy']:
            delay.append(queue[-1])
            queue.pop()
            server['busy'] = True
            server['counter'] = get_service_time(b)
            busy_slots += server['counter']

        # Update Statistical counters
        queue_size.extend([len(queue)]*event[0])

        slots_counter -= event[0]

    metrics = {}
    metrics['delay'] = delay
    metrics['queue_size'] = queue_size
    # The remaining time of the last packet in the server is removed by busy_slots since is not part
    # of the simulated slots.
    metrics['busy_slots'] = busy_slots - server['counter']
    metrics['p_overflow'] = float(discarded_pkts)/num_arrivals
    return metrics
