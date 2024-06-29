
---

# Visualizador de Bioinformática

Este proyecto es un visualizador interactivo de secuencias de alineamiento para aplicaciones de bioinformática. Utiliza Flask para la lógica del servidor web para la visualización de datos, permitiendo a los usuarios seleccionar diferentes algoritmos de alineamiento y explorar los resultados de manera dinámica.

## Características

- **Selección de Algoritmos:** Permite elegir entre varios algoritmos de alineamiento, incluyendo opciones como transformación a mayúsculas y búsqueda de coincidencias.
- **Visualización Interactiva:** Utiliza HTML, CSS y Js, y como Back Python ayudandonos de Flask para las visualizaciones interactivas que muestran los resultados de los alineamientos de manera clara y comprensible.
- **Integración de Datos:** Los usuarios pueden cargar secuencias de ADN, ARN o proteínas para visualizar y analizar sus alineamientos.
- **Resultados Detallados:** Cada algoritmo muestra resultados detallados, incluyendo coincidencias encontradas y ubicación de las mismas en las secuencias.

## Instalación

1. Clona este repositorio:

   ```
   git clone https://github.com/Ronald-Gutierrez/Visualizador-de-BioInfo.git
   ```

2. Instala las dependencias:

   ```
   pip install -r requirements.txt
   ```

## Uso

1. Ejecuta la aplicación Flask:

   ```
   python app.py
   ```

2. Abre tu navegador web y visita `http://localhost:5000`.

3. Selecciona el tipo de secuencia y el algoritmo de alineamiento deseado.

4. Ingresa las secuencias a analizar y presiona "Analizar".

5. Observa los resultados de los alineamientos visualizados en la interfaz.

## Contribución

Las contribuciones son bienvenidas. Si quieres contribuir a este proyecto, por favor sigue estos pasos:

1. Haz un fork del repositorio.
2. Crea una nueva rama (`git checkout -b feature-nueva-funcionalidad`).
3. Haz tus cambios.
4. Haz commit de tus cambios (`git commit -am 'Agrega nueva funcionalidad'`).
5. Haz push de tu rama (`git push origin feature-nueva-funcionalidad`).
6. Crea un pull request.

## Créditos

- Desarrollado por [Ronald Gutiérrez](https://github.com/Ronald-Gutierrez).

## Licencia

Este proyecto está licenciado bajo la Licencia MIT - consulta el archivo [LICENSE](LICENSE) para más detalles.

---
