from Bio import pairwise2
from Bio.Align import substitution_matrices

# Alinear dos secuencias utilizando una matriz de sustitución especificada
def align_sequences(seq1, seq2, matrix_name):
    # Cargar la matriz especificada
    matrix = substitution_matrices.load(matrix_name)
    # Realizar la alineación global
    alignments = pairwise2.align.globalds(seq1, seq2, matrix, -10.0, -0.5)
    return alignments

# Calcular métricas de alineación
def calculate_alignment_metrics(alignment):
    align1, align2, score, start, end = alignment
    length = len(align1)
    
    identity = sum(1 for a, b in zip(align1, align2) if a == b)
    similarity = sum(1 for a, b in zip(align1, align2) if a == b or (a != '-' and b != '-'))
    gaps = sum(1 for a, b in zip(align1, align2) if a == '-' or b == '-')
    
    identity_percentage = (identity / length) * 100
    similarity_percentage = (similarity / length) * 100
    gaps_percentage = (gaps / length) * 100
    
    return length, identity, similarity, gaps, identity_percentage, similarity_percentage, gaps_percentage

# Calcular el puntaje del alineamiento
def calculate_alignment_score(alignment):
    _, _, score, _, _ = alignment
    return score

# Guardar los resultados de la alineación en un archivo de texto
def format_alignment_output(alignment, matrix_name, block_size):
    output_lines = []
    align1, align2, score, _, _ = alignment
    
    # # Escribir las características
    # output_lines.append(f"# Matrix: {matrix_name}")
    # output_lines.append("# Gap_penalty: 10.0")
    # output_lines.append("# Extend_penalty: 0.5\n")
    
    # length, identity, similarity, gaps, identity_percentage, similarity_percentage, gaps_percentage = calculate_alignment_metrics(alignment)
    
    # output_lines.append(f"# Length: {length}")
    # output_lines.append(f"# Identity: {identity}/{length} ({identity_percentage:.1f}%)")
    # output_lines.append(f"# Similarity: {similarity}/{length} ({similarity_percentage:.1f}%)")
    # output_lines.append(f"# Gaps: {gaps}/{length} ({gaps_percentage:.1f}%)\n")
    
    for i in range(0, len(align1), block_size):
        output_lines.append(f"sequencia 1: {align1[i:i+block_size]}")
        output_lines.append(f"sequencia 2: {align2[i:i+block_size]}")
        
    return output_lines


