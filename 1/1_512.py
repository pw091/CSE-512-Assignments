import altair as alt
import pandas as pd

data = pd.DataFrame({'x':['A','B'], 'y':[5,3]})
alt.Chart(data).mark_bar().encode(x='x',y='y')
print(chart)