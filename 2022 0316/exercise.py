import pandas as pd
import matplotlib.pyplot as plt

catalog=pd.read_excel("2020 catalog.xlsx")

catalog.head()
catalog.columns
catalog.dtypes
catalog.isna().sum()
