class Genome(object):

    def __init__(self, p_gain, i_gain, d_gain):

        self.chromosome = {
            "p_gain": p_gain,
            "i_gain": i_gain,
            "d_gain": d_gain
        }

    def set_fitness_metric(self, fitness_metric):

        self.fitness_metric = fitness_metric

    def __str__(self):

        return "{0}, {1}, {2}".format(self.p_gain, self.i_gain, self.d_gain)