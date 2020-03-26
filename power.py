#
# Complete the 'reduceCapacity' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY model as parameter.
#

from math import ceil
import pandas as pd

def reduceCapacity(model):

    counts = {}

    for m in model:
        if m in counts:
            counts[m]+=1
        else:
            counts[m] = 1

    n = ceil(len(model)/2)

    model_col = []
    count_col = []

    for m, count in counts.items():
        model_col.append(m)
        count_col.append(count)

    df = pd.DataFrame({'model':model_col, 'counts':count_col})
    df = df.sort_values('counts', ascending=False)
    
    deactivated = 0
    n_models = 0

    while deactivated < n:
        deactivated += df.counts.iloc[n_models]
        n_models += 1

    return n_models
