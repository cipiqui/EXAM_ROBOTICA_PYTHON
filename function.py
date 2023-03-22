
# functions.py
# Carlos Ipiéns Quintanar
# Examen Python
# Fichero en el que se han implementado y probado las funciones

# Ejercicio 2
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

# Ejercicio 3
# Crear una funcion llamada split que reciba un diccionatio como el devuelto en read_data y devuelva dos diccionarios.
# En el primero se muestran las que tengan el valor white en el atributo type
# En el segundo se muestran las que tengan red en type
# En los diccionarios no aparecerá el atributo type

def split(data):
    data_white = {}
    data_red = {}
    for key in data:
        if data[key]['type'] == 'white':
            data_white[key] = {'fixed acidity': data[key]['fixed acidity'], 'volatile acidity': data[key]['volatile acidity'], 'citric acid': data[key]['citric acid'], 'residual sugar': data[key]['residual sugar'], 'chlorides': data[key]['chlorides'], 'free sulfur dioxide': data[key]['free sulfur dioxide'], 'total sulfur dioxide': data[key]['total sulfur dioxide'], 'density': data[key]['density'], 'pH': data[key]['pH'], 'sulphates': data[key]['sulphates'], 'alcohol': data[key]['alcohol'], 'quality': data[key]['quality']}
        else:
            data_red[key] = {'fixed acidity': data[key]['fixed acidity'], 'volatile acidity': data[key]['volatile acidity'], 'citric acid': data[key]['citric acid'], 'residual sugar': data[key]['residual sugar'], 'chlorides': data[key]['chlorides'], 'free sulfur dioxide': data[key]['free sulfur dioxide'], 'total sulfur dioxide': data[key]['total sulfur dioxide'], 'density': data[key]['density'], 'pH': data[key]['pH'], 'sulphates': data[key]['sulphates'], 'alcohol': data[key]['alcohol'], 'quality': data[key]['quality']}
    return data_white, data_red

"""
mostramos por pantalla los diccionarios devueltos por la funcion split
print(split(read_data('winequality.csv'))[0])
"""

# Ejercicio 4
# Crear una funcion llamada reduce que reciba un diccionario como el devuelto en la funcion split y un string que corresponda el nombre de un atributo,
# la funcion debe devolver una lista con los valores del atributo.
# Si el atributo no existe, devolverá un error de tipo ValueError

def reduce():
