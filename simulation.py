from society import Society

GENERATIONS = 10

society = Society(population_size=20)

for gen in range(GENERATIONS):
    society.form_groups()
    society.interactions()
    society.summary(gen)
