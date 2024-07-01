def buscar_subcadena(string_grande, subcadena):
    return subcadena in string_grande

def calcular_score(cadena1, cadena2):
    score = 0
    for char1, char2 in zip(cadena1, cadena2):
        if char1 == char2:
            score += 1
        else:
            score -= 2
    return score
