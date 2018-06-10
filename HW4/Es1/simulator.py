import numpy as np

def poisson(lambd):
	u = np.random.rand()
	i = 0
	p = np.exp(-lambd)
	F = p
	while u >= F:
		p *= lambd/(i+1)
		F += p
		i += 1
	return i

def exp_time(lambd):
	u = np.random.rand()
	return -np.log(u)/lambd

def get_service_time(p = 0.5):
	u = np.random.rand()
	if(u < p):
		return 1
	else:
		return 2

def run_queue(lambd):

	clock = 0
	queue = []
	server = 0
	# Event list : [next_arrival, next_dep]
	event_list = [np.inf, np.inf]
	delay = 0
	num_arrivals = 0
	idle_time = 0

	while(clock < 300000):
		if event_list[0] == np.inf:
			if event_list[1] == np.inf:
				clock += exp_time(lambd)
				# Add the departure time
				event_list[1] = clock + get_service_time()
				num_arrivals += 1
				idle_time += exp_time(lambd)
			else:
				# Generate an arrival
				event_list[0] = clock + exp_time(lambd)
				if(event_list[0] < event_list[1]): # Arrival
					clock = event_list[0]
					queue.append(clock)
					num_arrivals += 1
					event_list[0] = np.inf

				else: # Departure
					clock = event_list[1]
					if(not queue):
						event_list[1] = np.inf
					else:
						last_pkt = queue.pop()
						event_list[1] += get_service_time()
						delay += event_list[1] - last_pkt
		else: # An arrival is scheduled
			if event_list[1] == np.inf: # There's no departure scheduled => queue is empty
				idle_time += event_list[0] - clock
				clock = event_list[0]
				event_list[0] = np.inf
				event_list[1] = clock + get_service_time()
				num_arrivals += 1
			else:
				if event_list[0] < event_list[1]:
					# Arrival
					clock = event_list[0]
					queue.append(clock)
					num_arrivals += 1
					event_list[0] = np.inf
				else:
					# Departure
					clock = event_list[1]
					if(not queue):
						event_list[1] = np.inf
					else:
						last_pkt = queue.pop()
						event_list[1] += get_service_time()
						delay += event_list[1] - last_pkt
	return [delay/num_arrivals, (clock - idle_time)/clock]
