import pandas as pd
import numpy as np

def checkNull(d,z):
    print("Missing values in {d}:")
    print("Columns :", list(z.index))
    print("Rows :", list(d[d.isnull().any(axis=1)].index))
