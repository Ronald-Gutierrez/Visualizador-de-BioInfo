from flask import Flask, render_template, request
from algorithms.mayusculas import transform_to_uppercase  # type: ignore
from algorithms.mayusculas import transform_to_lowecase  # type: ignore
from algorithms.coincidencias import find_coincidences  # type: ignore
from algorithms.identificador_secuencia import identificar_secuencia  # type: ignore
from algorithms.transcripcion import transcripcion_adn_arn  # type: ignore
from algorithms.sub_cadena import buscar_subcadena  # type: ignore
from algorithms.sub_cadena import calcular_score  # type: ignore
from algorithms.alineamiento_global import needleman_wunsch_score, needleman_wunsch_alignment  # type: ignore
from algorithms.local_alignment import smith_waterman
from algorithms.clustering import clustering
from algorithms.star_alignment import needleman_wunsch_alignment_star,encontrar_secuencia_central


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('portada/home.html')

@app.route('/visualizador')
def index():
    return render_template('index.html')


@app.route('/analizar', methods=['POST'])
def analizar():
    # Obtener datos del formulario
    sequence1 = request.form.get('sequence1', '').upper()
    sequence2 = request.form.get('sequence2', '').upper()
    sequence = request.form.get('sequence', '').upper()
    # sequence_trans = request.form.get('sequence_trans', '')
    match = request.form.get('match', '')
    mismatch = request.form.get('mismatch', '')
    gap = request.form.get('gap', '')

    operation = request.form.get('operation', '')

    result = {}

    if operation == 'identificar_secuencia':
        # Llamar a la función de identificador de secuencia
        result = identificar_secuencia(sequence)
        cantidad = len(sequence)
        return render_template('identificador_sec.html', result=result, cantidad=cantidad,sequence=sequence, operation=operation)
    elif operation == 'transcripcion_adn_arn':
        result = transcripcion_adn_arn(sequence)
        return render_template('transcripcion.html', result=result, sequence=sequence, operation=operation)
    elif operation == 'sub_cadena':
        # Llamar a la función de subcadena
        score = calcular_score(sequence1, sequence2)
        sub_cadena = buscar_subcadena(sequence1, sequence2)
        return render_template('sub_cadena.html', score=score, sub_cadena=sub_cadena, sequence1=sequence1, sequence2=sequence2, operation=operation)
    elif operation == 'needleman_wunsch':
        # Convertir las entradas a enteros
        match = int(match)
        mismatch = int(mismatch)
        gap = int(gap)
        score = needleman_wunsch_score(
            sequence1, sequence2, match, mismatch, gap)
        alineaciones = needleman_wunsch_alignment(
            sequence1, sequence2, match, mismatch, gap)
        return render_template('alineamiento_global.html', score=score, alineaciones=alineaciones, sequence1=sequence1, sequence2=sequence2, match=match, mismatch=mismatch, gap=gap, operation=operation)
    elif operation == 'smith_waterman':
        match = int(match)
        mismatch = int(mismatch)
        gap = int(gap)

        result = smith_waterman(sequence1, sequence2, match, mismatch, gap)
        size = len(result)
        return render_template('local_alignment.html', sequence1=sequence1, sequence2=sequence2, match=match, mismatch=mismatch, gap=gap, result=result, size=size)
    
    elif operation =='star_alignment':
        match = int(match)
        mismatch = int(mismatch)
        gap = int(gap)
        additional_sequences = request.form.getlist('sequences[]')
        
        sequences = [sequence1, sequence2] + additional_sequences
        result = needleman_wunsch_alignment_star(sequences,match,mismatch,gap)
        find_secuencia_central = encontrar_secuencia_central(result)
        return render_template('star_alignment.html', sequences=sequences,find_secuencia_central=find_secuencia_central, sequence1=sequence1,sequence2=sequence2, additional_sequences=additional_sequences,result=result, match=match, mismatch=mismatch, gap=gap,operation=operation)


    elif operation == 'Clustering Distancia Mínima':
        matrix_input = request.form.get("distanceMatrix")
        matrix = []
        for row in matrix_input.splitlines():
            # Split each row by spaces and convert to integers
            matrix.append([float(num) for num in row.split()])
        clustering_result, matrices, min_distances = clustering(
            matrix, 'minimo')
        size = len(min_distances)
        result = list(enumerate(
            zip(clustering_result, matrices, min_distances), start=1))
        return render_template("single_linkage.html", matrix=matrix, result=result)
    elif operation == 'Clustering Distancia Máxima':
        matrix_input = request.form.get("distanceMatrix")
        matrix = []
        for row in matrix_input.splitlines():
            # Split each row by spaces and convert to integers
            matrix.append([float(num) for num in row.split()])
        clustering_result, matrices, max_distances = clustering(
            matrix, 'maximo')
        size = len(max_distances)
        result = list(enumerate(
            zip(clustering_result, matrices, max_distances), start=1))
        return render_template("complete_linkage.html", matrix=matrix, result=result)
    elif operation == 'Clustering Distancia Promedio':
        matrix_input = request.form.get("distanceMatrix")
        matrix = []
        for row in matrix_input.splitlines():
            # Split each row by spaces and convert to integers
            matrix.append([float(num) for num in row.split()])
        clustering_result, matrices, avg_distances = clustering(
            matrix, 'promedio')
        size = len(avg_distances)
        result = list(enumerate(
            zip(clustering_result, matrices, avg_distances), start=1))
        return render_template("average_linkage.html", matrix=matrix, result=result)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
