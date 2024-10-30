# Imports

import math
import pickle

import numpy as np
import pandas as pd


from sklearn.model_selection import train_test_split

#Funciones
def cargar_data(name): #Cargar los archivos de datos .dat
    data = pd.read_csv(f'data/{name}.dat', sep='::', names=['movie_id', 'title', 'genres'], engine='python')
    return data

