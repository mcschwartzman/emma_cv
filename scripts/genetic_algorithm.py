import random

from genome import Genome

print("initializing genetic algorithm")

class GeneticAlgorithm(object):

    def __init__(self, population_cap, generation_size):

        self.population_cap = population_cap
        self.generation_size = generation_size
        self.mutation_chance = 0.1
        self.population = []

    def initialize_population(self):

        unevaluated = []

        for i in range(self.population_cap):

            unevaluated.append(Genome(random.random(), random.random(), random.random()))

        self.unevaluated = unevaluated

    def evaluate_genomes(self, desired_value):

        for genome in self.unevaluated:

            # fitness metric evaluated manually
            product = genome.chromosome['p_gain'] * genome.chromosome['i_gain'] * genome.chromosome['d_gain']

            # current fitness metric is "how close is the product of p*i*d to some desired value"
            # SO, over time we should see the total populations get smaller and smaller and smaller
            # will likely bottom out at the fitness metric of the initial generation's best fit 
            # THIS IS WHY WE NEED MUTATION

            fitness_metric = desired_value - product

            genome.set_fitness_metric(fitness_metric)

            self.population.append(genome)

        # print(self.population)



    def sort_population(self):

        # sort population by the smallest fitness metric

        self.population = sorted(self.population, key=lambda genome: genome.fitness_metric)

        # print(self.population)

    def cull_population(self):

        index = -1 * self.generation_size

        self.population = self.population[:index]

        self.unevaluated = []

        return

    def new_generation(self):

        if len(self.population) >= self.population_cap:

            print("population is at cap! exiting...")

            return

        new_generation_size = self.population_cap - len(self.population)

        for i in range(self.generation_size):

            # we want to basically cull by the generation_size,
            # then add back that generation_size, so we can cull 6/8, then regen 6

            parents = random.sample(self.population, 2)

            child_1 = self.crossover_pair(parents[0], parents[1])

            self.unevaluated.append(child_1)

    def crossover_pair(self, parent_a, parent_b):

        # Construct a new genome from a random pairing of the genes from the parents

        new_p = random.choice([parent_a.chromosome['p_gain'], parent_b.chromosome['p_gain']])
        new_i = random.choice([parent_a.chromosome['i_gain'], parent_b.chromosome['i_gain']])
        new_d = random.choice([parent_a.chromosome['d_gain'], parent_b.chromosome['d_gain']])

        result = Genome(new_p, new_i, new_d)

        if random.random() < self.mutation_chance:
            # okay we're mutating!
            # which gene would you like to mutate?

            print("MUTATING")

            gene_to_mutate = random.choice(['p_gain', 'i_gain', 'd_gain'])

            result.chromosome[gene_to_mutate] = random.random() # needs to match how we generate genes in initialize_population

        return result

