from flask import Flask, render_template, request
from algorithms.mayusculas import transform_to_uppercase  # type: ignore
from algorithms.mayusculas import transform_to_lowecase  # type: ignore
from algorithms.coincidencias import find_coincidences  # type: ignore
from algorithms.idenntificador_secuencia import identificar_secuencia  # type: ignore
from algorithms.transcripcion import transcripcion_adn_arn  # type: ignore
from algorithms.sub_cadena import buscar_subcadena  # type: ignore
from algorithms.sub_cadena import calcular_score  # type: ignore


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analizar', methods=['POST'])
def analizar():
    # Obtener datos del formulario
    sequence1 = request.form.get('sequence1', '')
    sequence2 = request.form.get('sequence2', '')
    sequence = request.form.get('sequence', '')
    # sequence_trans = request.form.get('sequence_trans', '')

    operation = request.form.get('operation', '')

    result = {}
    
    # if operation == 'mayusculas':
    #     # Llamar a la función de mayúsculas
    #     result = transform_to_uppercase(sequence1, sequence2)
    #     result2 = transform_to_lowecase(sequence1, sequence2)
    #     return render_template('mayusculas.html', result=result, result2=result2, sequence1=sequence1, sequence2=sequence2, operation=operation)
    # elif operation == 'coincidencias':
    #     # Llamar a la función de coincidencias
    #     result = find_coincidences(sequence1, sequence2)
    #     return render_template('coincidencias.html', result=result, sequence1=sequence1, sequence2=sequence2, operation=operation)
    if operation == 'identificar_secuencia':
        # Llamar a la función de identificador de secuencia
        result = identificar_secuencia(sequence)
        return render_template('identificador_sec.html', result=result, sequence=sequence, operation=operation)
    elif operation == 'transcripcion_adn_arn':
        result = transcripcion_adn_arn(sequence)
        return render_template('transcripcion.html', result=result, sequence=sequence, operation=operation)
    elif operation == 'sub_cadena':
        # Llamar a la función de subcadena
        score = calcular_score(sequence1, sequence2)
        sub_cadena = buscar_subcadena(sequence1, sequence2)
        return render_template('sub_cadena.html', score=score, sub_cadena=sub_cadena, sequence1=sequence1, sequence2=sequence2, operation=operation)
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
