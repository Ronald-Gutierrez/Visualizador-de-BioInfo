import numpy as np
import matplotlib.pyplot as plt

def dot_matrix(seq1, seq2):
    points = []
    for i in range(len(seq1)):
        for j in range(len(seq2)):
            if seq1[i] == seq2[j]:
                points.append((i, j))
    return points

def plot_dot_matrix(points, seq1, seq2, filepath, markersize=15, labelsize=10, background_color='white', line_color='grey'):
    fig, ax = plt.subplots()

    # Dibujar puntos en color gris
    for p in points:
        ax.plot(p[1], p[0], color=line_color, marker='.', markersize=markersize)

    # Unir puntos que forman diagonales
    for i in range(1, len(seq1)):
        for j in range(1, len(seq2)):
            if (i-1, j-1) in points and (i, j) in points:
                ax.plot([j-1, j], [i-1, i], color=line_color, linewidth=2.5) 

    ax.set_xticks(np.arange(len(seq2)))
    ax.set_yticks(np.arange(len(seq1)))

    ax.set_yticklabels(seq1[::1], fontsize=labelsize)  # Invertir seq1 para que coincida con el eje y invertido
    ax.xaxis.tick_top()  # Colocar el eje x arriba

    ax.invert_yaxis()  # Invertir el eje y

    # Colocar etiquetas de seq2 en el eje derecho
    ax.yaxis.set_label_position('right')
    ax.set_xticklabels(seq2, fontsize=labelsize, rotation=0)

    ax.tick_params(axis='both', which='major', labelsize=labelsize)

    # Cambiar el color de fondo
    ax.set_facecolor(background_color)

    plt.savefig(filepath)
    plt.close()
