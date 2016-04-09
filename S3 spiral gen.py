import plotly.plotly as py

py.sign_in('whitequill','9sw1pbyxdu')

import plotly.graph_objs as go
from math import sin,cos,sqrt,e
import pandas as pd

s0 = []
s1 = []
s2 = []

f = str(filename)
def datagen(t, pmax, step):
    while (t < pmax):
         S1 = (2/3)*cos((sqrt(3)*t)/2)*e**(t/2) + 1/(3*e**t)
         S2 = (1/3*cos(sqrt(3)/2*t)+(1/sqrt(3))*sin((sqrt(3)/2)*t))*e**(t/2) + (-1)/(3*e**t)
         S3 = (-1/3*cos(sqrt(3)/2*t)+(1/sqrt(3))*sin((sqrt(3)/2)*t))*e**(t/2) + 1/(3*e**t)
         t = t + step

         value = S1, S2, S3
         ss0 = pd.Series(S1, index=s0.append(S1))
         ss1 = pd.Series(S2, index=s1.append(S2))
         ss2 = pd.Series(S3, index=s2.append(S3))

#         p0s = str(s0)
#         p1s = str(s1)
#         p2s = str(s2)

#   print(p0s + ", " + p1s + ", " + p2s)
#   print(str(ss0) + ", " + str(ss1) + ", " + str(ss2))
    print("Plottable data has been generated.")

    trace1 = go.Scatter3d(  x=s0,
                            y=s1,
                            z=s2
                            )
    Data = [trace1]
    Layout = go.Layout(
        title='S3 Spiral Plot'
    )
    fig = go.Figure(data=Data, layout=Layout)
    py.plot(fig, filename=f)



 
            

