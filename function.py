
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
                data['dato'+str(len(data)+1)] = {'type': row[0], 'fixed acidity': row[1], 'volatile acidity': row[2], 'citric acid': row[3], 'residual sugar': row[4], 'chlorides': row[5], 'free sulfur dioxide': row[6], 'total sulfur dioxide': row[7], 'density': row[8], 'pH': row[9], 'sulphates': row[10], 'alcohol': row[11], 'quality': row[12]}
    return data

"""
mostramos por pantalla el diccionario devuelto
print(read_data('winequality.csv'))
"""

# Funcion 2
# Crear una funcion llamada split que reciba un diccionatio como el devuelto en read_data y devuelva dos diccionarios.
# En el primero se muestran 