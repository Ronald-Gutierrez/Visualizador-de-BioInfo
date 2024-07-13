import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram

def distance_min(matrix, clusters, strategy):
    min_dist = float('inf')
    min_pair = (0, 0)
    for i in range(len(matrix)):
        for j in range(i + 1, len(matrix[i])):
            if matrix[i][j] < min_dist:
                min_dist = matrix[i][j]
                min_pair = (i, j)
    return min_pair, min_dist


def update_matrix(matrix, clusters, pair, strategy):
    new_matrix = []
    for i in range(len(matrix)):
        if i != pair[0] and i != pair[1]:
            new_row = []
            for j in range(len(matrix)):
                if j != pair[0] and j != pair[1]:
                    new_row.append(matrix[i][j])
            new_matrix.append(new_row)

    if strategy == 'minimo':
        new_row = [min(matrix[pair[0]][i], matrix[pair[1]][i])
                   for i in range(len(matrix)) if i != pair[0] and i != pair[1]]
    elif strategy == 'maximo':
        new_row = [max(matrix[pair[0]][i], matrix[pair[1]][i])
                   for i in range(len(matrix)) if i != pair[0] and i != pair[1]]
    elif strategy == 'promedio':
        new_row = [(matrix[pair[0]][i] + matrix[pair[1]][i]) /
                   2 for i in range(len(matrix)) if i != pair[0] and i != pair[1]]

    new_row.append(0.0)
    for row in new_matrix:
        row.append(new_row[new_matrix.index(row)])
    new_matrix.append(new_row)

    return new_matrix


def clustering(matrix, strategy):
    clusters = [[{i}] for i in range(len(matrix))]
    current_matrix = matrix
    result_clusters = [clusters.copy()]
    result_matrices = [matrix.copy()]
    min_distances = []

    while len(clusters) > 1:
        (i, j), min_dist = distance_min(current_matrix, clusters, strategy)
        new_cluster = clusters[i] + clusters[j]

        clusters = [clusters[k]
                    for k in range(len(clusters)) if k != i and k != j]
        clusters.append(new_cluster)

        current_matrix = update_matrix(
            current_matrix, clusters, (i, j), strategy)

        result_clusters.append(clusters.copy())
        result_matrices.append(current_matrix.copy())
        min_distances.append(min_dist)
        print(min_dist)

    return result_clusters, result_matrices, min_distances

    