def find_coincidences(sequence1, sequence2):
    len1 = len(sequence1)
    len2 = len(sequence2)
    
    # Inicializar lista de caracteres coincidentes
    matching_chars = []
    
    # Iterar sobre ambas secuencias y encontrar coincidencias
    for i in range(min(len1, len2)):
        if sequence1[i] == sequence2[i]:
            matching_chars.append(sequence1[i])
    
    return matching_chars
