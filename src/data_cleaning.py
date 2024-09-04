import pandas as pd

def load_data(file_path):
    """Carga el conjunto de datos desde un archivo CSV."""
    return pd.read_csv(file_path, encoding='ISO-8859-1')

def clean_data(df):
    """Limpia el conjunto de datos eliminando duplicados y manejando valores nulos."""
    print("Valores nulos antes de la limpieza:")
    print(df['Spotify Popularity'].isnull().sum())  # Verifica valores nulos antes de limpiar
    
    # Eliminar filas con valores nulos en 'Spotify Popularity' y duplicados
    df_cleaned = df.dropna(subset=['Spotify Popularity']).drop_duplicates()
    
    print("Valores nulos después de la limpieza:")
    print(df_cleaned['Spotify Popularity'].isnull().sum())  # Verifica valores nulos después de limpiar
    
    return df_cleaned

def normalize_column(df, column_name):
    """Normaliza una columna numérica en el conjunto de datos."""
    if column_name in df.columns:
        # Normalización min-max para escalar los datos entre 0 y 1
        df[column_name + '_normalized'] = (df[column_name] - df[column_name].min()) / (df[column_name].max() - df[column_name].min())
        print(df[column_name + '_normalized'].head())  # Verifica los primeros valores normalizados
    else:
        print(f"La columna '{column_name}' no se encuentra en el DataFrame.")
    return df

if __name__ == "__main__":
    # Cargar el dataset
    df = load_data('../data/most_streamed_songs_2024.csv')
    print("Columnas del DataFrame:", df.columns)
    
    # Limpieza de datos
    df_cleaned = clean_data(df)
    
    # Normalización de la columna 'Spotify Popularity'
    df_cleaned = normalize_column(df_cleaned, 'Spotify Popularity')
    
    # Guardar el DataFrame limpio y normalizado
    df_cleaned.to_csv('../data/most_streamed_songs_2024_cleaned.csv', index=False)
