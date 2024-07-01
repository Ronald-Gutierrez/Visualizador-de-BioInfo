def transcripcion_adn_arn(secuencia_adn):
    # Convertir la secuencia de ADN a mayúsculas
    secuencia_adn = secuencia_adn.upper()
    
    # Definir el diccionario de transcripción de ADN a ARN
    transcripcion = {
        'A': 'U',
        'T': 'A',
        'C': 'G',
        'G': 'C'
    }
    
    # Inicializar la secuencia de ARN resultante
    secuencia_arn = ""
    
    # Convertir cada base de ADN a su base complementaria de ARN
    for base in secuencia_adn:
        if base in transcripcion:
            secuencia_arn += transcripcion[base]
        else:
            # Manejar caracteres no válidos
            secuencia_arn += "N"  # 'N' indica una base no identificada
    
    return secuencia_arn
