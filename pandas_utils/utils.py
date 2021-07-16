import pandas as pd

def myjoin(a, b, on, how, **kwargs):
    return (a.set_index(on).join(b.set_index(on), how=how, **kwargs).reset_index())

def fraction_nans_in_column(df, column):
    count_nan = len(df[column]) - df[column].count()
    return count_nan/float(len(df[column]))
