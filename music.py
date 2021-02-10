    boundaries = []
    individual_points = []
    for j in range(0,2 + 1):
        for i in range(color[j] - z, color[j] + z + 1):
            individual_points.append(i)
        boundaries.append(individual_points)
        individual_points = []
    print(boundaries)