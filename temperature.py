#
# Complete the 'predictTemperature' function below.
#
# The function is expected to return a FLOAT_ARRAY.
# The function accepts following parameters:
#  1. STRING startDate
#  2. STRING endDate
#  3. FLOAT_ARRAY temperature
#  4. INTEGER n
#

from datetime import datetime, timedelta
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

def predictTemperature(startDate, endDate, temperature, n):

    # convert startDate to datetime
    dt = datetime.fromisoformat(startDate)
    endDate = datetime.fromisoformat(endDate)

    p = len(temperature)

    # create list of datetimes for each hour of data
    times = []
    for _ in range(int(p)):
        times.append(dt)
        dt += timedelta(hours=1)
    
    # create temperature pandas dataframe
    temps = pd.DataFrame({'datetime':times, 'temp':temperature})

    temps['hour'] = temps['datetime'].apply(lambda x: x.hour)
    temps['day'] = temps['datetime'].apply(lambda x: x.day)

    

    model = LinearRegression()
    features = ['day']
    target = 'temp'

    # creating x_pred
    x_pred = np.linspace(endDate.day+1, endDate.day+1+n, n)
    x_pred = x_pred.reshape(-1,1)

    temp_res = []

    for i in range(24):
        filtered = temps[temps['hour']==i]

        X = filtered[features]
        y = filtered[target]

        model.fit(X,y)
        temp_res.append(model.predict(x_pred))
    
    res = []

    for i in range(n):
        for entry in temp_res:
            res.append(entry[i])

    return res