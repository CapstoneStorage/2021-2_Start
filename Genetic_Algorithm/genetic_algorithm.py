# y = w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5 + w6*x6
# x1=4 x2=-2 x3=7 x4=5 x5=11 x6=1

import numpy
import matplotlib.pyplot

# fitness가 놓을 수록 좋은 solution
def cal_pop_fitness(equation_inputs, pop):
    # 현 세대에서 적합도를 계산
    # input과 weight 들의 합을 구함
    fitness = numpy.sum(pop*equation_inputs, axis = 1)
    return fitness;

# 자식을 생성할 가장 좋은 부모를 고른다.
def select_mating_pool(pop, fitness, num_parents):
    parents = numpy.empty((num_parents, pop.shape[1]))
    for parent_num in range(num_parents):
        max_fitness_idx = numpy.where(fitness == numpy.max(fitness))
        max_fitness_idx = max_fitness_idx[0][0]
        parents[parent_num, :] = pop[max_fitness_idx, :]
        fitness[max_fitness_idx] = -99999999999
    return parents

# 교차
def crossover(parents, offspring_size):
    offspring = numpy.empty(offspring_size)
    #부모의 교차 발생 지점 (주로 가운데)
    crossover_point = numpy.uint8(offspring_size[1]/2)
    for k in range(offspring_size[0]):
        # 교배할 부모1
        parent1_idx = k%parents.shape[0]
        # 교배할 부모2
        parent2_idx = (k+1)%parents.shape[0]
        # 자손의 반쪽은 부모1로부터
        offspring[k, 0:crossover_point] = parents[parent1_idx, 0:crossover_point]
        # 자손의 반쪽은 부모2로부터
        offspring[k, crossover_point:] = parents[parent2_idx, crossover_point:]
    return offspring
 
# 돌연변이는 자손의 유전자 하나를 랜덤하게 바꾼다
def mutation(offspring_crossover, num_mutations = 1):
    mutations_counter = numpy.uint8(offspring_crossover.shape[1] / num_mutations)
    for idx in range(offspring_crossover.shape[0]):
        gene_idx = mutations_counter - 1
        for mutation_num in range(num_mutations):
            # 랜덤한 수를 gene에 더함
            random_value = numpy.random.uniform(-1.0, 1.0, 1)
            offspring_crossover[idx, gene_idx] = offspring_crossover[idx, gene_idx] + random_value
            gene_idx = gene_idx + mutations_counter
    return offspring_crossover
    

# 입력 값
equation_inputs = [4, -2, 3.5, 5, -11, -4.7]
# Weight의 개수 (optimize하고자 하는 parameter)
num_weights = len(equation_inputs)

# 세대 별 해의 개수
sol_per_pop = 8
# 교배하는 부모의 수
num_parents_mating = 4

# Population size
# 염색체의 개수: sol_per_pop, 염색제 속 유전자의 개수: num_weights
pop_size = (sol_per_pop, num_weights)
# 초기 인구수
# (sol_per_pop, num_weights)
new_population = numpy.random.uniform(low=-4.0, high=4.0, size=pop_size)

best_outputs = []
# 세대 수
num_generations = 1000
for generation in range(num_generations):
    print("세대: ", generation)
    # Population에서 염색체의 적합도를 평가
    fitness = cal_pop_fitness(equation_inputs, new_population)
    print("적합도: ")
    print(fitness)
    
    best_outputs.append(numpy.max(numpy.sum(new_population*equation_inputs, axis = 1)))
    print("최선의 결과: ", numpy.max(numpy.sum(new_population*equation_inputs, axis = 1)))
    # population에서 최적의 부모 찾기
    parents = select_mating_pool(new_population, fitness, num_parents_mating)
    #print("부모: ")
    #print(parents)
    # 교차를 이용하여 다음 세대 생성
    offspring_crossover = crossover(parents, offspring_size = (pop_size[0] - parents.shape[0], num_weights))
    #print("교차: ")
    #print(offspring_crossover)
    # 돌연변이를 통해 자손에 변화를 줌
    offspring_mutation = mutation(offspring_crossover, num_mutations = 2)
    #print("돌연변이: ")
    #print(offspring_mutation)
    # 부모와 자손을 통해서 새로운 세대를 생성
    new_population[0:parents.shape[0], :] = parents
    new_population[parents.shape[0]:, :] = offspring_mutation

fitness = cal_pop_fitness(equation_inputs, new_population)
best_match_idx = numpy.where(fitness == numpy.max(fitness))

print("최적해: ", new_population[best_match_idx, :])
print("최적해의 적합도: ", fitness[best_match_idx])

# 그래프
matplotlib.pyplot.plot(best_outputs)
matplotlib.pyplot.xlabel("Iteration")
matplotlib.pyplot.ylabel("Fitness")
matplotlib.pyplot.show()
    
