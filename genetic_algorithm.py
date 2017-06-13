from Graph import *
import random
import numpy as np
import pickle


def generating_population(graph,population_size):

    nodes = graph.list_nodes
    population = np.zeros(shape=(1, len(nodes)))

    for i in range(population_size):
        new_individual = [random.randint(0, len(nodes)) for _ in range(0, len(nodes))]
        new_individual = np.array(new_individual)
        new_individual = np.reshape(new_individual,newshape=(1,len(new_individual)))
        population = np.append(population,new_individual,axis=0)
    population = np.delete(population, 0, 0)

    return population


def population_evaluation(graph,population):

    evaluated = []
    for individual in population:
        wrongly_colored = 0
        node = 0
        try:
            individual = list(individual)
            for gene in individual:
                neighbours = graph.get_neighbours(node)

                for neighbour in neighbours:
                    neighbour_color = individual[neighbour]
                    if neighbour_color == gene:
                        wrongly_colored += 1
                node += 1
        except TypeError:
            print(individual,'tutaj blad wtf')
            break
        evaluated.append(wrongly_colored)

    try:
        best_individual = evaluated.index(min(evaluated))
        best_individual = population[best_individual]
        best_individual_errorValue = min(evaluated)
    except ValueError:
        best_individual_errorValue = 0
        best_individual = population[0]

    return evaluated,best_individual,best_individual_errorValue


def roulette(graph,population,evaluated):

    population_size = population.shape[0]
    num_of_nodes = len(graph.list_nodes)
    individuals_probabilities = np.zeros(shape=(population_size,2))
    selected = np.zeros(shape=(1, num_of_nodes))

    for i in range(population_size):
        try:
            probability = evaluated[i]
            probability = (len(graph.list_nodes)-probability)/len(graph.list_nodes)
            individuals_probabilities[i,1] = probability
            individuals_probabilities[i+1,0] = probability
        except IndexError:
            break


    for i in range(population.shape[0]):
        random_probabiity = random.random()
        if  random_probabiity < individuals_probabilities[i,1] and random_probabiity > individuals_probabilities[i,0]:
            individual = np.reshape(population[i], newshape=(1, len(population[i])))
            selected = np.append(selected,individual,axis=0)


    if np.array_equal(selected,np.zeros(shape=(1, num_of_nodes))):
        # print("nothing was selected")
        selected = population
    else:
        selected = np.delete(selected, 0, 0)

    return selected


def crossing(selected):

    crossed = np.zeros(shape=(1, selected.shape[1]))
    crossing_probability_low = 0.6
    crossing_probability_high = 0.8
    try:
        how_many_selected = selected.shape[0]
    except IndexError:
        how_many_selected = 125


    for i in range(0,selected.shape[0],2):
        random_probabiity = random.random()
        if random_probabiity > crossing_probability_low and random_probabiity < crossing_probability_high:
            try:
                individual1 = selected[i,:]
                individual2 = selected[i+1,:]
                part1_ind1 = individual1[0:(int(len(individual1)/2-1))]
                part1_ind2 = individual2[0:(int(len(individual1)/2-1))]
                part2_ind1 = individual1[(int(len(individual1)/2-1)):]
                part2_ind2 = individual2[(int(len(individual1)/2-1)):]
                crossed_ind1 = np.hstack((part1_ind1,part2_ind2))
                crossed_ind2 = np.hstack((part1_ind2,part2_ind1))
                crossed_ind1 = np.reshape(crossed_ind1,newshape=(1,len(crossed_ind1)))
                crossed_ind2 = np.reshape(crossed_ind2,newshape=(1,len(crossed_ind2)))
                crossed = np.append(crossed,crossed_ind1,axis=0)
                crossed = np.append(crossed,crossed_ind2,axis=0)
            except IndexError:
                break

    if np.array_equal(crossed,np.zeros(shape=(1, selected.shape[1]))):
        # print("crossing could not be performed")
        crossed = selected
    else:
        crossed = np.delete(crossed, 0, 0)

    return crossed


def mutation(crossed):

    mutation_probability = 0.01
    mutated = np.zeros(shape=(1, crossed.shape[1]))
    for individual in crossed:
        individual_shape = individual.shape
        for gene in individual:
            random_probabiity = random.random()
            if random_probabiity < mutation_probability:
                individual = np.reshape(individual,newshape=individual_shape)
                individual = list(individual)
                individual[individual.index(gene)] = random.randint(0, crossed.shape[1])
                individual = np.array(individual)
                individual = np.reshape(individual, newshape=(1, len(individual)))
                crossed = np.delete(crossed,individual,0)
                mutated = np.append(mutated,individual,axis=0)

    if np.array_equal(mutated,np.zeros(shape=(1, crossed.shape[1]))):
        # print("nothing was mutated")
        mutated_population = crossed
    else:
        mutated = np.delete(mutated, 0, 0)
        mutated_population = np.append(crossed,mutated)


    return mutated_population


def genetic_algorithm(graph, initial_population_size):

    population = generating_population(graph,initial_population_size)
    best_ind_errorValue = 1

    while best_ind_errorValue > 0:
        evaluated,best_individual,best_ind_errorValue = population_evaluation(graph,population)
        selected = roulette(graph,population,evaluated)
        crossed = crossing(selected)
        mutated = mutation(crossed)
        population = mutated

    print(best_individual)
    return best_individual

if __name__ == '__main__':
    with open('genetics_graph_ready.pkl','rb') as file:
        g = pickle.load(file)
    best_individual = genetic_algorithm(g, 300)
    with open('best_individual.pkl','wb') as file:
        pickle.dump(best_individual,file)
