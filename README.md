# Most Streamed Spotify Songs 2024

Este proyecto realiza un análisis detallado de las canciones más reproducidas en Spotify durante 2024. A través de técnicas de ciencia de datos, hemos limpiado y preprocesado los datos, realizado un análisis exploratorio detallado, y desarrollado un modelo predictivo para entender mejor qué factores influyen en la popularidad de las canciones.

## Contenido del Proyecto

- **data/**: Contiene los datasets en formato CSV, incluyendo el dataset original y el dataset limpio.
- **notebooks/**: Incluye notebooks de Jupyter utilizados para análisis exploratorio de datos (EDA) y modelado predictivo.
- **src/**: Contiene scripts Python para la limpieza de datos (`data_cleaning.py`) y visualización de datos (`data_visualization.py`).
- **reports/**: Documentos y presentaciones generadas a partir del análisis.
- **README.md**: Descripción general del proyecto y guías de uso.
- **requirements.txt**: Lista de dependencias necesarias para ejecutar el proyecto.

## Requisitos

Para ejecutar este proyecto, necesitas tener instalado Python 3.x y las siguientes bibliotecas:

- `pandas`
- `numpy`
- `matplotlib`
- `seaborn`
- `scikit-learn`

Puedes instalar las dependencias ejecutando el siguiente comando:

pip install -r requirements.txt 


Estructura del Proyecto

most-streamed-spotify-songs-2024/
│
├── data/                          # Carpeta para los datasets
│   ├── most_streamed_songs_2024.csv
│   └── most_streamed_songs_2024_cleaned.csv
│
├── notebooks/                     # Carpeta para los notebooks de Jupyter
│   └── data_analysis.ipynb
│
├── src/                           # Carpeta para scripts de Python
│   ├── data_cleaning.py
│   └── data_visualization.py
│
├── reports/                       # Carpeta para la presentación y otros informes
│   └── presentation.pdf
│
├── README.md                      # Descripción general del proyecto
├── requirements.txt               # Lista de dependencias de Python
└── .gitignore                     # Archivos a ignorar en Git


Uso
Sigue estos pasos para ejecutar el proyecto:

Clona el repositorio:

git clone https://github.com/SanMaBruno/most-streamed-spotify-songs-2024.git
cd most-streamed-spotify-songs-2024

Instala las dependencias:

pip install -r requirements.txt

Ejecuta los scripts de análisis:

Limpieza de datos:

python src/data_cleaning.py

Visualización de datos:

python src/data_visualization.py

Abre el notebook de Jupyter para análisis exploratorio de datos:

jupyter notebook notebooks/data_analysisExplora los notebooks:

Abre y explora notebooks/data_analysis.ipynb para ver el análisis exploratorio de datos y el modelado predictivo.
Resultados Clave
Distribución de la Popularidad: La mayoría de las canciones tienen una popularidad normalizada alta, lo que sugiere que los hits más populares tienen características comunes.
Artistas Dominantes: Artistas como Bad Bunny, Drake, y Taylor Swift son los más representados en las listas, posiblemente debido a estrategias de marketing efectivas y una gran base de seguidores.
Modelo Predictivo: El modelo de regresión lineal alcanzó un error cuadrático medio (MSE) de 0.0151, indicando una capacidad moderada para predecir la popularidad basada en características seleccionadas.
Contribuciones
Las contribuciones son bienvenidas. Para contribuir:

Haz un fork del proyecto.
Crea una nueva rama (git checkout -b feature/nueva-funcionalidad).
Haz commit de tus cambios (git commit -m 'Agregar nueva funcionalidad').
Haz push a la rama (git push origin feature/nueva-funcionalidad).
Abre un Pull Request.
Licencia
Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.

Contacto
Si tienes preguntas o comentarios, por favor contacta a SanMaBruno.

