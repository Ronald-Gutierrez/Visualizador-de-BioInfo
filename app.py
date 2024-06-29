from flask import Flask, render_template, request
from algorithms.mayusculas import transform_to_uppercase # type: ignore
from algorithms.coincidencias import find_coincidences # type: ignore

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analizar', methods=['POST'])
def analizar():
    # Obtener datos del formulario
    sequence1 = request.form['sequence1']
    sequence2 = request.form['sequence2']
    operation = request.form['operation']
    
    result = {}
    
    if operation == 'mayusculas':
        # Llamar a la función de mayúsculas
        result = transform_to_uppercase(sequence1, sequence2)
        return render_template('mayusculas.html', result=result)
    elif operation == 'coincidencias':
        # Llamar a la función de coincidencias
        result = find_coincidences(sequence1, sequence2)
        return render_template('coincidencias.html', result=result, sequence1=sequence1, sequence2=sequence2, operation=operation)
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
