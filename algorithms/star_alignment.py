def needleman_wunsch_alignment_star(sequences, match, mismatch, gap):
    n = len(sequences)
    matriz_puntuacion_final = [[0] * (n + 1) for _ in range(n + 1)]

    def needleman_wunsch(sequence1, sequence2):
        len1 = len(sequence1)
        len2 = len(sequence2)

        matriz_puntuacion = [[0] * (len2 + 1) for _ in range(len1 + 1)]

        for i in range(1, len1 + 1):
            matriz_puntuacion[i][0] = matriz_puntuacion[i - 1][0] + gap
        for j in range(1, len2 + 1):
            matriz_puntuacion[0][j] = matriz_puntuacion[0][j - 1] + gap

        for i in range(1, len1 + 1):
            for j in range(1, len2 + 1):
                score_diag = matriz_puntuacion[i - 1][j - 1] + (match if sequence1[i - 1] == sequence2[j - 1] else mismatch)
                score_up = matriz_puntuacion[i - 1][j] + gap
                score_left = matriz_puntuacion[i][j - 1] + gap

                matriz_puntuacion[i][j] = max(score_diag, score_up, score_left)

        return matriz_puntuacion[len1][len2]

    sequence_labels = [""] + [f"S{i + 1}" for i in range(n)]
    matriz_puntuacion_final[0] = sequence_labels[:]
    for i in range(1, n + 1):
        matriz_puntuacion_final[i][0] = sequence_labels[i]

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == j:
                matriz_puntuacion_final[i][j] = "-"
            else:
                score = needleman_wunsch(sequences[i - 1], sequences[j - 1])
                matriz_puntuacion_final[i][j] = str(score)

    return matriz_puntuacion_final

def encontrar_secuencia_central(matriz_puntuacion_final):
    n = len(matriz_puntuacion_final) - 1 
    max_sum = 0
    central_sequence = None

    for i in range(1, n + 1):
        sum_distance = 0
        for j in range(1, n + 1):
            if i != j and matriz_puntuacion_final[i][j] != "-":  
                sum_distance += int(matriz_puntuacion_final[i][j])  

        if sum_distance > max_sum:
            max_sum = sum_distance
            central_sequence = matriz_puntuacion_final[i][0]  

    return central_sequence, max_sum
