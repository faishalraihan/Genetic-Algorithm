# Faishal Raihanur Rasyid-1301184163-IF4204
import random
import copy
import math


def generatePopulation(population_size, kromosom_size):
    population = []
    for i in range(population_size):
        kromosom = []
        for i in range(kromosom_size*2):
            #kromosom.append(random.randint(0, 9))
            kromosom.append(random.randint(0, 1))
        population.append(kromosom)

    return population


def decodeKromosom(kromosom):
    ###################Representasi Biner###################################
    x1 = -1 + (3 / (2 ** -1 + 2**-2+2**-3 + 2**-4 + 2**-5)) * \
        ((kromosom[0]*2**-1)+(kromosom[1]*2**-2) +
         (kromosom[2]*2**-3)+(kromosom[3]*2**-4) + (kromosom[4]*2**-5))
    x2 = -1 + (2 / (2 ** -1 + 2**-2+2**-3 + 2**-4 + 2**-5)) * \
        ((kromosom[5]*2**-1)+(kromosom[6]*2**-2) +
         (kromosom[7]*2**-3)+(kromosom[8]*2**-4) + (kromosom[9]*2**-5))
    ##################Representasi Integer##################################
    # x1 = -1 + (3 / (9 * (10**-1 + 10**-2 + 10**-3 + 10**-4+ 10**-5))) * \
    #     ((kromosom[0]*10**-1)+(kromosom[1]*10**-2) +
    #      (kromosom[2]*10**-3)+(kromosom[3]*10**-4) + (kromosom[4]*10**-5))
    # x2 = -1 + (2 / (9 * (10**-1 + 10**-2 + 10**-3 + 10**-4 + 10**-4+ 10**-5))) * \
    #     ((kromosom[5]*10**-1)+(kromosom[6]*10**-2) +
    #      (kromosom[7]*10**-3)+(kromosom[8]*10**-4) + (kromosom[9]*10**-5))

    return [x1, x2]


def FitnessFunction(kromosom):
    d = decodeKromosom(kromosom)
    b = random.random()
    fitness = (math.cos(d[0]) * math.sin(d[1])) - (d[0] / (d[1]**2 + 1))
    if (b > fitness):
        # print("b: ",b)
        # print("fitness: ",fitness)
        fitness = b - fitness
    else:
        b = random.uniform(fitness, fitness+0.1)
        # print("b: ",b)
        # print("fitness: ",fitness)
        fitness = b - fitness
    #fitness = -((math.cos(d[0]) * math.sin(d[1])) - (d[0] / (d[1]**2 + 1)))
    #fitness = 1 / ((math.cos(d[0]) * math.sin(d[1])) - (d[0] / (d[1]**2 + 1)) +  0.01)
    return fitness


def FitnessAll(population, population_size):
    fitness_all = []
    for i in range(population_size):
        fitness_all.append(FitnessFunction(population[i]))
    return fitness_all


def tournamentSelection(population, uktour, population_size):
    best_kromosom = []
    for i in range(0, uktour-1):
        kromosom = population[random.randint(0, population_size-1)]
        if (best_kromosom == [] or FitnessFunction(kromosom) > FitnessFunction(best_kromosom)):
            best_kromosom = kromosom
    return best_kromosom


def rouletteWheel(fitnessAll, population_size):
    total = 0
    rfit = 0
    for i in range(0, population_size-1):
        total += fitnessAll[i]
        #print("total: ",total)
    for j in range(0, population_size-1):
        rfit += fitnessAll[j]/total
        #print("rfit: ",rfit)
    r = random.uniform(0, rfit)
    kromosom = 0
    while(r > 0 and kromosom < population_size-1):
        r -= fitnessAll[kromosom]/total
        kromosom += 1
    return kromosom


def SinglePointcrossover(parent1, parent2, pc):

    r = random.random()
    if (r <= pc):
        point = random.randint(0, 9)
        for i in range(point):
            parent1[i], parent2[i] = parent2[i], parent1[i]

    return parent1, parent2


def DoublePointcrossover(parent1, parent2, pc):
    r = random.random()
    if(r <= pc):
        point1 = random.randint(0, 9)
        point2 = random.randint(0, 9)
        for i in range(point1+1, point2-1):
            parent1[i], parent2[i] = parent2[i], parent1[i]

    return parent1, parent2


def mutasi(children1, children2, pm):
    r = random.random()
    r1 = random.randint(0, 9)
    r2 = random.randint(0, 9)
    if (r <= pm):
        if(children1[r1] == 0 and children2[r2] == 0):
            children1[r1] == 1
            children2[r2] = 1
        elif(children1[r1] == 1 and children2[r2] == 1):
            children1[r1] = 0
            children2[r2] = 0
        elif(children1[r1] == 0):
            children1[r1] = 1
        elif(children1[r1] == 1):
            children1[r1] = 0
        elif(children2[r2] == 0):
            children1[r2] = 1
        else:
            children2[r2] = 0
    ######## For Integer ######################################
    # children1[r1] = random.randint(0, 9)
    # children2[r2] = random.randint(0, 9)
    return children1, children2


def Elitism(population_size, fitnessAll):
    return fitnessAll.index(max(fitnessAll))


population_size = 50
kromosom_size = 5
uktour = 5
generation = 20
pc = 0.6
pm = 0.01

population = generatePopulation(population_size, kromosom_size)
# print(population)
for i in range(generation):
    #print("i: ", i)
    fitness = FitnessAll(population, population_size)
    #print("Nilai Fitness: ", fitness)
    newPopulation = []
    best = Elitism(population_size, fitness)
    # print(best)
    #print("Fitness Terbaik: ", fitness[best])
    if(population_size % 2 != 0):
        newPopulation.append(population[best])
        # print(newPopulation)
    else:
        newPopulation.append(population[best])
        newPopulation.append(population[best])
        # print(newPopulation)
    j = 0
    while (j < population_size-1):
        #print("j: ", j)
        parent1 = rouletteWheel(fitness, population_size)
        parent2 = rouletteWheel(fitness, population_size)
        # parent1 = tournamentSelection(population, uktour, population_size)
        # parent2 = tournamentSelection(population, uktour, population_size)
        while (parent1 == parent2):
            # parent2 = tournamentSelection(population, uktour, population_size)
            parent2 = rouletteWheel(fitness, population_size)
        # print("Parent1: ", parent1)
        # print("Parent2: ", parent2)
        # par1 = copy.deepcopy(parent1)
        # par2 = copy.deepcopy(parent2)
        par1 = population[parent1]
        par2 = population[parent2]
        children = DoublePointcrossover(par1, par2, pc)
        children = mutasi(children[0], children[1], pm)
        # print(children)
        newPopulation += children
        j += 2
    population = newPopulation
    # x = len(population)
    # print("Jumlah population setelah mutasi: ", x)
    #print("population: ",population)
newFitness = FitnessAll(population, population_size)
# print(newFitness)
result = Elitism(population_size, newFitness)
dcd = decodeKromosom(population[result])

#print('Best Fitness :', FitnessFunction(population[result]))
print('Best Chromosome: ', population[result])
print("x1: ", dcd[0], "x2: ", dcd[1])
