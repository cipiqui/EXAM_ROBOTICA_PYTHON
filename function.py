
# functions.py
# Carlos Ipiéns Quintanar
# Examen Python
# Fichero en el que se han implementado y probado las funciones

# Función 1
# Crear una función read_data que reciba el nombre de un csv y devuleva un diccionario con cada muestra del csv,
# donde la clave de cada subdiccionario irá incrementando desdde dato1. Si hay alguna muestra con un dato vacío no
# se insertará en el diccionario

def read_data(wine_quality):
    import csv
    with open(wine_quality) as f:
        lectorFichero = csv.reader(f)
        cabecera = next(lectorFichero)
        data = {}
        for row in lectorFichero:
            if row[0] != '':
                data['dato'+str(len(data)+1)] = {'fixed acidity': row[0], 'volatile acidity': row[1], 'citric acid': row[2], 'residual sugar': row[3], 'chlorides': row[4], 'free sulfur dioxide': row[5], 'total sulfur dioxide': row[6], 'density': row[7], 'pH': row[8], 'sulphates': row[9], 'alcohol': row[10], 'quality': row[11]}
    return data
    