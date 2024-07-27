import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
from scipy.spatial.distance import squareform

def get_clustering_levels(dist_matrix, Z):
    num_clusters = len(dist_matrix)
    labels = [chr(ord('A') + i) for i in range(num_clusters)]
    
    # Lista que mapea índices de clusters a etiquetas
    cluster_labels = [[label] for label in labels]
    
    result = ""
    for i, (cluster1, cluster2, dist, _) in enumerate(Z):
        new_cluster_label = cluster_labels[int(cluster1)] + cluster_labels[int(cluster2)]
        result += f'Nivel {i+1}: Cluster {"".join(cluster_labels[int(cluster1)])} se une con Cluster {"".join(cluster_labels[int(cluster2)])} a una distancia de {dist:.4f}\n'
        
        # Actualizar el mapeo de clusters
        cluster_labels.append(new_cluster_label)
    
    return result

def read_distance_matrix(filepath):
    with open(filepath, 'r') as file:
        lines = file.readlines()
    dist_matrix = np.array([list(map(float, line.strip().split())) for line in lines])
    return dist_matrix

def compute_linkage(dist_matrix):
    dist_vector = squareform(dist_matrix, checks=False)
    Z = linkage(dist_vector, 'average')
    return Z

def calculate_distances_and_differences(Z):
    avg_distances = []
    differences = []
    previous_dist = None

    for i, (cluster1, cluster2, dist, _) in enumerate(Z):
        if previous_dist is not None:
            difference = dist - previous_dist
            differences.append(difference)
        avg_distance = dist / 2  
        avg_distances.append(avg_distance)
        previous_dist = dist

    return avg_distances, differences

def plot_dendrogram_with_distances(Z, labels, avg_distances, differences, filepath):
    plt.figure(figsize=(12, 8))
    ddata = dendrogram(Z, labels=labels, leaf_rotation=0, leaf_font_size=12, orientation='right', no_plot=False)
    
    for i, (cluster1, cluster2, dist, _) in enumerate(Z):
        x_coords = ddata['icoord'][i]
        y_coords = ddata['dcoord'][i]
        
        x = y_coords[1]
        y = (x_coords[1] + x_coords[2]) / 2
        
        plt.text(x + 1, y - 1, f'{dist:.2f}', va='center', ha='center', fontsize=10, color='red')
        plt.plot(x, y, 'o', markersize=8, color='black')
        
        if i < len(avg_distances):
            avg_dist = avg_distances[i]
            plt.text(x - 4.5, y - 4, f' {avg_dist:.2f}', va='center', ha='left', fontsize=8, color='green')
        if i < len(differences):
            diff = differences[i]
            plt.text(x + 1, y + 1, f' {diff:.2f}', va='center', ha='left', fontsize=8, color='purple')
    
    plt.xticks(range(1, int(Z[-1][2])+1)) 
    plt.grid(axis='x', linestyle='--', alpha=0.7)
    plt.savefig(filepath)
    plt.close()  # Asegúrate de cerrar la figura aquí

# def main():
#     filepath_input = 'algorithms/input.txt'
#     filepath_output = 'static/result_img/upgma.png'

#     dist_matrix = read_distance_matrix(filepath_input)
#     Z = compute_linkage(dist_matrix)
#     clustering_levels = get_clustering_levels(dist_matrix, Z)
    
#     print(clustering_levels)
    
#     avg_distances, differences = calculate_distances_and_differences(Z)
#     labels = [chr(ord('A') + i) for i in range(len(dist_matrix))]
    
#     plot_dendrogram_with_distances(Z, labels, avg_distances, differences, filepath_output)

# if __name__ == "__main__":
#     main()
