from algorithms.alineamiento_global import globalTraceback, needleman_wunsch_score


def needleman_wunsch_alignment_star(sequences, match, mismatch, gap):
    n = len(sequences)
    matriz_puntuacion_final = [[0] * (n + 1) for _ in range(n + 1)]

    def needleman_wunsch(sequence1, sequence2):
        len1 = len(sequence1)
        len2 = len(sequence2)

        # Convertir secuencias a minúsculas
        sequence1 = sequence1.lower()
        sequence2 = sequence2.lower()

        matriz_puntuacion = [[0] * (len2 + 1) for _ in range(len1 + 1)]

        for i in range(1, len1 + 1):
            matriz_puntuacion[i][0] = matriz_puntuacion[i - 1][0] + gap
        for j in range(1, len2 + 1):
            matriz_puntuacion[0][j] = matriz_puntuacion[0][j - 1] + gap

        for i in range(1, len1 + 1):
            for j in range(1, len2 + 1):
                # Comparar en minúsculas
                score_diag = matriz_puntuacion[i - 1][j - 1] + (
                    match if sequence1[i - 1] == sequence2[j - 1] else mismatch)
                score_up = matriz_puntuacion[i - 1][j] + gap
                score_left = matriz_puntuacion[i][j - 1] + gap

                matriz_puntuacion[i][j] = max(score_diag, score_up, score_left)

        return matriz_puntuacion[len1][len2], sequence1, sequence2

    sequence_labels = [""] + [f"S{i + 1}" for i in range(n)]
    matriz_puntuacion_final[0] = sequence_labels[:]
    for i in range(1, n + 1):
        matriz_puntuacion_final[i][0] = sequence_labels[i]

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == j:
                matriz_puntuacion_final[i][j] = "-"
            else:
                score, _, _ = needleman_wunsch(
                    sequences[i - 1], sequences[j - 1])
                matriz_puntuacion_final[i][j] = str(score)

    return matriz_puntuacion_final


def encontrar_secuencia_central(matriz_puntuacion_final):
    n = len(matriz_puntuacion_final)
    max_sum = float('-inf')
    central_sequence = None
    central_index = 0
    for i in range(1, n):
        sum_distance = 0
        for j in range(1, n):
            if i != j and matriz_puntuacion_final[i][j] != '-':
                sum_distance += int(matriz_puntuacion_final[i][j])

        if sum_distance > max_sum:
            max_sum = sum_distance
            central_sequence = matriz_puntuacion_final[i][0]
            central_index = i-1
    return central_sequence, max_sum, central_index


def pairwise_distance(seq1, seq2, match, mismatch, gap):
    score, _ = needleman_wunsch_score(seq1, seq2, match, mismatch, gap)
    return score


def align_to_center(sequences, center_index, match, mismatch, gap):
    center_sequence = sequences[center_index]
    aligned_sequences = []
    for i, seq in enumerate(sequences):
        if i != center_index:
            _, dp = needleman_wunsch_score(
                center_sequence, seq, match, mismatch, gap)
            align = globalTraceback(
                dp, center_sequence, seq, match, mismatch, gap)
            # align1, align2, _ = needleman_wunsch(center_sequence, seq)
            aligned_sequences.append(align[-1])
    return aligned_sequences


def merge_alignments(center_seq, aligned_sequences):
    msa = [center_seq]
    for center_aligned, seq_aligned in aligned_sequences:
        if len(center_aligned) > len(msa[0]):
            msa = [s.ljust(len(center_aligned), '-') for s in msa]
        elif len(center_aligned) < len(msa[0]):
            center_aligned = center_aligned.ljust(len(msa[0]), '-')
            seq_aligned = seq_aligned.ljust(len(msa[0]), '-')
        msa.append(seq_aligned)
    return msa
