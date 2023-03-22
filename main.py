
# main.py
# Carlos Ipiéns Quintanar
# Examen Python
# Fichero de llamada a las funciones

# Importamos function para poder hacer las llamadas a las funciones
import function

# Llamada a la primera funcion
print("La funcion read_data devolverá: ")
print(function.read_data('winequality.csv'))

# Llamada a la segunda funcion
print("La funcion split devolverá: ")
print(function.split(function.read_data('winequality.csv')))

# Llamada a la tercera funcion
print("La funcion reduce devolverá: ")
print(function.reduce(function.split(function.read_data('winequality.csv'))[0], 'alcohol'))


