import pandas as pd

df = pd.read_table('../pre_processing/ementas_acordaos', header=None, encoding='utf-8')
print(df.info())
print(df.head())
