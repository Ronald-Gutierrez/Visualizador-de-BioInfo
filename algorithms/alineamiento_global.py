def needleman_wunsch_score_matrix(seq1, seq2, match_score, mismatch_score, gap_penalty):
    len_seq1 = len(seq1)
    len_seq2 = len(seq2)
    
    # Inicializar la matriz de puntuaciones y la matriz de rastreo
    score_matrix = [[0] * (len_seq1 + 1) for _ in range(len_seq2 + 1)]
    
    # Inicializar la primera fila y la primera columna con penalizaciones de espacio
    for i in range(1, len_seq1 + 1):
        score_matrix[0][i] = score_matrix[0][i-1] + gap_penalty
    for j in range(1, len_seq2 + 1):
        score_matrix[j][0] = score_matrix[j-1][0] + gap_penalty
    
    # Llenar la matriz de puntuaciones
    for i in range(1, len_seq2 + 1):
        for j in range(1, len_seq1 + 1):
            if seq1[j-1] == seq2[i-1]:
                diagonal_score = score_matrix[i-1][j-1] + match_score
            else:
                diagonal_score = score_matrix[i-1][j-1] + mismatch_score
            
            left_score = score_matrix[i][j-1] + gap_penalty
            up_score = score_matrix[i-1][j] + gap_penalty
            
            # Determinar el máximo de los puntajes posibles
            max_score = max(diagonal_score, left_score, up_score)
            score_matrix[i][j] = max_score
    
    return score_matrix