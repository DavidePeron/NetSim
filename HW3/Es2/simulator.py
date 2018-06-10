import numpy as np


class Simulator:

    num_sim = 100
    alpha = 0.5
    b = 6 #dB
    sigma = 8#dB
    R = 1 # radius of the approximating circle for the intended cell
    eta = 3.5 #dB
    rf = 1

    # distances R1 and R2 for reuse factors = 1, 3, 4, 7
    # 0 stands for the tx cell
    rf_array = np.array([0, 1, 3, 4, 7])
    distances_bounds = np.array([[0, 1], [0.68, 2.41], [2, 4], [2.06, 3.47], [3.24, 4.91]])

    def binomial(self, n, p):
        pr = (1 - p)**n
        c = p/(1-p)
        u = np.random.rand()
        i = 0
        F = pr
        while u >= F:
            pr *= c*(n-i)/(i+1)
            F += pr
            i += 1
        return i

    def exponential(self, _lambda = 1):
        return -np.log(np.random.rand())/_lambda

    def get_interf_distances(self):
        return self.distances_bounds[np.where(self.rf_array == self.rf)]

    def generate_node(self):
        distances = self.get_interf_distances() # Returns a matrix in the form [[R1, R2]]
        return np.sqrt((distances[0][1]**2 - distances[0][0]**2)*np.random.rand() + distances[0][0]**2)

    # In this case R2 = 1, R1 = 0
    def generate_user(self):
        return self.R*np.sqrt(np.random.rand())

    def get_snr(self, r0, k = None):
        snr_num = self.exponential() * np.exp(self.sigma * np.random.randn())
        snr_den = 0
        if k == None:
            k = self.binomial(6, self.alpha)

        if k != 0:
            for i in range(k):
                snr_den += self.exponential() * np.exp(self.sigma * np.random.randn()) * (float(r0)/self.generate_node())**self.eta
            return float(snr_num)/snr_den
        else:
            return 10**(self.b/10) + 1

    def get_success_probability(self, n = None):
        success_probability = 0
        for _ in range(self.num_sim):
            # Generate the user node
            r_0 = self.generate_user()
            if self.get_snr(r_0, n)> 10**(self.b/10):
                success_probability += 1
        return success_probability/self.num_sim

    def get_outage(self):
        return round(1 - self.get_success_probability(), 3)

    def get_capture(self, n):
        return round(n*self.get_success_probability(n), 3)
