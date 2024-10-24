import pandas as pd

def OneHotEncoder(dataframe, category):
  df_encoded = pd.get_dummies(data, columns=[category, ])
  return df_encoded
