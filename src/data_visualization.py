import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def plot_popularity_distribution(df):
    """Grafica la distribución de la popularidad normalizada de las canciones en Spotify."""
    plt.figure(figsize=(10, 6))
    sns.histplot(df['Spotify Popularity_normalized'], bins=30, kde=True)  # Histograma con curva KDE para la distribución
    plt.title('Distribución de la Popularidad Normalizada de Canciones en Spotify')
    plt.xlabel('Popularidad Normalizada')
    plt.ylabel('Frecuencia')
    plt.show()

def plot_top_artists(df, top_n=10):
    """Grafica un diagrama de barras de los top N artistas con más canciones."""
    plt.figure(figsize=(12, 8))
    sns.countplot(y=df['Artist'], order=df['Artist'].value_counts().index[:top_n])  # Ordenar por los artistas más frecuentes
    plt.title(f'Top {top_n} Artistas con Más Canciones')
    plt.xlabel('Número de Canciones')
    plt.ylabel('Artista')
    plt.show()

if __name__ == "__main__":
    # Cargar el conjunto de datos limpio
    df = pd.read_csv('../data/most_streamed_songs_2024_cleaned.csv')
    
    # Visualizaciones
    plot_popularity_distribution(df)
    plot_top_artists(df)
