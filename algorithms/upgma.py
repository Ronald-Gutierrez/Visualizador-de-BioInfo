import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
from scipy.spatial.distance import squareform

def save_clustering_levels(dist_matrix, Z, output_file):

    with open(output_file, 'w') as file:
        for i, (cluster1, cluster2, dist, _) in enumerate(Z):
            file.write(f'Nivel {i+1}: Cluster {int(cluster1+1)} se une con Cluster {int(cluster2+1)} a una distancia de {dist:.4f}\n')

# Leer la matriz de distancias desde input.txt
with open('input.txt', 'r') as file:
    lines = file.readlines()

# Convertir el contenido del archivo en una matriz de distancias
dist_matrix = np.array([list(map(float, line.strip().split())) for line in lines])

# Convertir la matriz de distancias en una forma de vector
dist_vector = squareform(dist_matrix, checks=False)

# Cálculo del linkage usando el método UPGMA (average linkage)
Z = linkage(dist_vector, 'average')

# Guardar los niveles de clúster y las distancias en output.txt usando la función
save_clustering_levels(dist_matrix, Z, 'output.txt')

# Calcular distancias promedio y diferencias
avg_distances = []
differences = []
previous_dist = None

for i, (cluster1, cluster2, dist, _) in enumerate(Z):
    if previous_dist is not None:
        difference = dist - previous_dist
        differences.append(difference)
    avg_distance = dist / 2  # Promedio de distancia para cada clúster
    avg_distances.append(avg_distance)
    previous_dist = dist

# Crear el dendrograma con etiquetas y distancias
labels = [chr(ord('A') + i) for i in range(len(dist_matrix))]  # Genera etiquetas desde 'A' hasta el número de elementos

plt.figure(figsize=(12, 8))

# Función personalizada para agregar etiquetas de distancia y puntos en las uniones
def plot_dendrogram_with_distances(Z, labels, avg_distances, differences):
    # Genera el dendrograma
    ddata = dendrogram(Z, labels=labels, leaf_rotation=0, leaf_font_size=12, orientation='right', no_plot=False)
    
    # Obtener coordenadas
    for i, (cluster1, cluster2, dist, _) in enumerate(Z):
        x_coords = ddata['icoord'][i]
        y_coords = ddata['dcoord'][i]
        
        # Coordenada x de la distancia
        x = y_coords[1]
        # Coordenada y del medio de la unión
        y = (x_coords[1] + x_coords[2]) / 2
        
        # Añadir la distancia al gráfico
        plt.text(x + 1, y - 1, f'{dist:.2f}', va='center', ha='center', fontsize=10, color='red')
        
        # Añadir un punto en la unión
        plt.plot(x, y, 'o', markersize=8, color='black')
        
        # Añadir etiquetas de distancia promedio y diferencia
        if i < len(avg_distances):
            avg_dist = avg_distances[i]
            plt.text(x - 4.5, y - 4, f' {avg_dist:.2f}', va='center', ha='left', fontsize=8, color='green')
        if i < len(differences):
            diff = differences[i]
            plt.text(x + 1, y + 1, f' {diff:.2f}', va='center', ha='left', fontsize=8, color='purple')
    
    return ddata

plot_dendrogram_with_distances(Z, labels, avg_distances, differences)

# Ajustes del gráfico
plt.xticks(range(1, int(Z[-1][2])+1))  # Añadir marcas en el eje x
plt.grid(axis='x', linestyle='--', alpha=0.7)  # Añadir líneas de rejilla

# Guardar el dendrograma en un archivo
plt.savefig('upgma_horizontal.png')

# # Mostrar el gráfico
# plt.show()
