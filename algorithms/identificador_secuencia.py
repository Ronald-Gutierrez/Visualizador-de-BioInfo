def identificar_secuencia(secuencia):
    # Definir los caracteres válidos para cada tipo de secuencia
    caracteres_adn = set("ATGC")
    caracteres_arn = set("AUGC")
    caracteres_proteina = set("ACDEFGHIKLMNPQRSTVWY")

    # Convertir la secuencia a mayúsculas
    secuencia = secuencia.upper()

    # Crear un conjunto de caracteres en la secuencia
    caracteres_secuencia = set(secuencia)

    # Inicializar la variable de resultado
    resultado = None

    # Comprobar si la secuencia es de ADN
    if caracteres_secuencia.issubset(caracteres_adn):
        resultado = "ADN"
    # Comprobar si la secuencia es de ARN
    elif caracteres_secuencia.issubset(caracteres_arn):
        resultado = "ARN"
    # Comprobar si la secuencia es de Proteína
    elif caracteres_secuencia.issubset(caracteres_proteina):
        resultado = "Proteína"
    else:
        resultado = "Secuencia no reconocida"

    return resultado

