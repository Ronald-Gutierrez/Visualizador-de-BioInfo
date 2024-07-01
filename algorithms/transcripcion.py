def transcripcion_adn_arn(secuencia):
    nueva_secuencia = ''
    palabras = secuencia.split()  
    
    for palabra in palabras:
        primera_letra = palabra[0]  
        if primera_letra == 'T':
            nueva_secuencia += 'U'
        else:
            nueva_secuencia += primera_letra
    return nueva_secuencia