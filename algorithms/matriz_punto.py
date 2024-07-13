import numpy as np
import matplotlib.pyplot as plt

def dot_matrix(seq1, seq2):
    points = []
    for i in range(len(seq1)):
        for j in range(len(seq2)):
            if seq1[i] == seq2[j]:
                points.append((i, j))
    return points

def plot_dot_matrix(points, seq1, seq2, filepath, markersize=20, labelsize=12):
    fig, ax = plt.subplots()

    # Dibujar puntos en color gris
    for p in points:
        ax.plot(p[1], p[0], color='gray', marker='.', markersize=markersize)

    # Unir puntos que forman diagonales
    for i in range(1, len(seq1)):
        for j in range(1, len(seq2)):
            if (i-1, j-1) in points and (i, j) in points:
                ax.plot([j-1, j], [i-1, i], color='gray', linewidth=3) 

    ax.set_xticks(np.arange(len(seq2)))
    ax.set_yticks(np.arange(len(seq1)))

    ax.set_yticklabels(seq1[::1], fontsize=labelsize)  
    ax.xaxis.tick_top()  
    ax.invert_yaxis()  

    # Colocar etiquetas de seq2 en el eje derecho
    ax.yaxis.set_label_position('right')
    ax.set_xticklabels(seq2, fontsize=labelsize, rotation=0)

    ax.tick_params(axis='both', which='major', labelsize=labelsize)
    plt.savefig(filepath)
    plt.close()

# Ejemplo de secuencias
seq1 = "ACGT"
seq2 = "ACGT"

# Crear la lista de puntos
points = dot_matrix(seq1, seq2)

# Ruta para guardar la imagen
filepath = 'static/result_img/matriz_puntos.png'

# Generar y guardar la gráfica
plot_dot_matrix(points, seq1, seq2, filepath, labelsize=13)  # Puedes ajustar labelsize según lo necesites
