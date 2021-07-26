import pandas as pd

def myjoin(a, b, on, how, **kwargs):
    return (a.set_index(on).join(b.set_index(on), how=how, **kwargs).reset_index())

def fraction_nans_in_column(df, column):
    count_nan = len(df[column]) - df[column].count()
    return count_nan/float(len(df[column]))

def column_from_df(df, column, min_entries = 1):
    assert min_entries > 0, "min entries must be non negative"
    if min_entries == 1:
        return set(df[column])
    else:
        temp = df.groupby(column).size().reset_index()
        temp = temp.loc[temp[0] >= min_entries]
    return set(temp[column])

def fraction_nans_in_df(df):
    count_nan = len(df) - df.count()
    return count_nan/float(len(df))

def add_quantiles(df, source_col, target_col):
    column = df[source_col]
    q_values = list(column.quantile([0.0, 0.25, 0.5, 0.75]))
    # Make q_values unique
    q_values = list(set(q_values))
    quantiles = column.apply(lambda x: bisect.bisect_left(q_values, x))
    df[target_col] = quantiles
