def calcular_score(cadena1, cadena2):
    score = 0
    for char1, char2 in zip(cadena1, cadena2):
        if char1.lower() == char2.lower():
            score += 1
        else:
            score -= 2
    return score

def buscar_subcadena(string_grande, subcadena):
    return subcadena.lower() in string_grande.lower()  
