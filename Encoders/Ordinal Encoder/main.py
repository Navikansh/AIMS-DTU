import pandas as pd


def OrdinalEncoder(dataframe, orderedvars, category):
  mapping = {}
  j = 0
  for i in orderedvars:
    mapping[i] = j
    j++
  dataframe[category] = dataframe[category].replace(mapping)
  return dataframe
    


