import numpy as np

def poisson(_lambda):
    #CDF Inversion
    mean_CDF = 0
    u = np.random.rand()
    i = 0
    _lambda = float(_lambda)
    p = np.exp(-_lambda)
    F = p
    while u >= F:
        p *= _lambda/(i+1)
        F += p
        i += 1
    return i

# pos = coordinates of the actual node
# R = radius of the circle in which points are generated
def get_neighbor(actual_node, R = 1):
    neighbor = {}
    #Angle of the new point
    a = np.random.rand() * 2 * np.pi
    #Radius of the new point (between 0 and 1)
    r = R * np.sqrt(np.random.rand())
    x_new = actual_node[0] + r * np.cos(a)
    y_new = actual_node[1] + r * np.sin(a)
    return np.array([x_new, y_new, np.sqrt(x_new**2 + y_new**2)])

def make_hop(actual_node, M):
    new_node = actual_node
    while new_node[2] >= actual_node[2]:
        # If there are no candidate relays within range, retry (in the next slot)
        n = poisson(M)
        if(n==0):
            return new_node

        neighbors = np.empty((n, 3))
        for _ in range(0,n):
            neighbors[_] = get_neighbor(actual_node)
        new_node = neighbors[np.argmin(neighbors[:,2])]
    return new_node

def run(D, M):
    # Generate a random position for the transmitter node
    alpha = np.random.rand() * 2 * np.pi
    x_tx = D * np.cos(alpha)
    y_tx = D * np.sin(alpha)
    node = np.array([x_tx, y_tx, D])

    n_hop = 1
    while node[2] > 1:
        node = make_hop(node, M)
        n_hop += 1
    return n_hop
