from society import Society

GENERATIONS = 30

society = Society(population_size=20, world_size=10)

for gen in range(GENERATIONS):
    print(f"\n--- Generation {gen} ---")
    society.form_groups()
    society.step()
    society.conflict()
    society.world.regenerate()
    society.summary()
