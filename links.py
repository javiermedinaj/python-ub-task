import pandas as pd

def get_links(file_path):
    # Lee el archivo CSV
    links_df = pd.read_csv(file_path)

    # Extracción de valores por fila
    links_list = links_df.iloc[:, 2:].values.flatten().tolist()

    # Filtrar valores nulos (NaN)
    links_list = [link for link in links_list if pd.notna(link)]

    # Concatenar los enlaces en una cadena separada por saltos de línea
    links_text = '\n'.join(links_list)

    return links_text

if __name__ == "__main__":
    file_path = 'links.csv'
    links_text = get_links(file_path)

    # Guardar los enlaces en un archivo de texto
    with open('enlaces.txt', 'w') as f:
        f.write(links_text)

    print("Los enlaces se han guardado correctamente en 'enlaces.txt'")
