import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import os
np.set_printoptions(precision=3, suppress=True)

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

column_names = ['Number_1', 'Number_2', 'Sum']
path = "random_numbers.csv" 
raw_dataset = pd.read_csv(path, names=column_names,
                          na_values='?', comment='\t',
                          sep=' ', skipinitialspace=True)

dataset = raw_dataset.copy()
print(dataset.tail())
