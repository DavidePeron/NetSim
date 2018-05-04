import numpy as np

def check_arrivals_in_next_slot(a):
    coin = np.random.rand()
    #Check for at least 1 arrival
    if(coin < 2*a):
        #Check for only 1 arrival
        if(coin < a):
            return 1
        else:
            return 2
    return 0

# Return a list with:
# - (int) distance from the next useful slot
# - (Bool) departure if True
# - (int) number of arrivals
def next_event(a, queue, server):
    event = [1, False, 0]

    # Check for departure
    if server == True:
        event[2] = check_arrivals_in_next_slot(a)
        event[1] = True
        return event

    # Iterate until an arrival
    arrival = False
    while(not arrival):
        event[0] += 1
        event[2] = check_arrivals_in_next_slot(a)
        if(event[2] > 0):
            arrival = True
    return event

def run_queue(slots_counter, a):

    #Metrics
    queue_size = [0]
    delay = []
    num_arrivals = 0
    discarded_pkts = 0

    queue = []
    server = False

    while(slots_counter > 0):

        # Generate next event
        event = next_event(a, queue, server)

        # Update arrivals
        # Insert a packet (an int starting from 1 that increase at each iteration and indicates the number of slots that they remain in the queue)
        for _ in range(0,event[2]):
            queue.insert(0,0)

        # Update departures
        server = False
        # If the queue is not empty, serve the last element
        if queue:
            delay.append(queue[-1])
            queue.pop()
            server = True

        # Update packet's delay
        queue = [pkt+1 for pkt in queue]

        # Update Statistical counters
        queue_size.extend([len(queue)]*event[0])

        slots_counter -= event[0]

    metrics = {}
    metrics['delay'] = delay
    metrics['queue_size'] = queue_size
    return metrics
