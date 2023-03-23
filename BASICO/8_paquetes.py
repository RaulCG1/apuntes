#manage package

#pip
# PIP https://pypi.org

# pip install pip
# pip --version
# pip install numpy

#import pandas
import numpy as np

print(np.version.version)


arreglo= np.array([1,2,3,4,5,6])

print(arreglo.max())

import pandas as pd

arreglo_pandas =pd.Series([1,2,3,4,5,6])

print(arreglo_pandas)

#pip install requests

import requests as rq

peticion = rq.get('https://pokeapi.co/api/v2/pokemon?limit=151')

print(peticion)
print(peticion.status_code)
print(peticion.json())

#paqute de aritmetico
from mypackage import arhitmetics
print(arhitmetics.suma_two_number(10,10))