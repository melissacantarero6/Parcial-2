#Ejemplo 1

import pandas as pd

# Se crea el dataframe
data = {
    'Nombre': ['Alice', 'Bob', 'Charlie'],
    'Edad': [25, 30, 35],
    'Ciudad': ['New York', 'Los Angeles', 'Chicago']
}

df = pd.DataFrame(data)

# Se muestra el dataframe
print("DataFrame creado:")
print(df)


#########################################################################

#Ejemplo 2

import pandas as pd


# Se crea un DataFrame
data = {
    'Nombre': ['Alice', 'Bob', 'Charlie'],
    'Edad': [25, 30, 35],
    'Ciudad': ['New York', 'Los Angeles', 'Chicago']
}

df = pd.DataFrame(data)

# Filtramos  los datos para mostrar solo los que cumplen con la condición
mayores_de_30 = df[df['Edad'] > 30]

# Mostral
print("Empleados mayores de 30 años:")
print(mayores_de_30)
