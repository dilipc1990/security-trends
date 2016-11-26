import plotly.plotly as plotly
import plotly
from plotly.graph_objs import Scatter, Layout
import pandas as pd

plotly.offline.init_notebook_mode(connected=True)

df = pd.read_csv('/Users/shramesh/Documents/Shankara/SourceCode/Python/CI-Project/data_2012.csv')

for col in df.columns:
    df[col] = df[col].astype(str)


layout = dict(
    title = '2012 Global Threats Attack Number',
    geo = dict(
        showframe = False,
        showcoastlines = False,
        projection = dict(
            type = 'Mercator'
        )
    )
)

df['YEAR'] = df['YEAR'] +' - '+ df['COUNT']+' <br>'


data = [ dict(
        type = 'choropleth',
        locations = df['CODE'],
        z = df['Attack Count'],
        text = df['YEAR'],
        colorscale = [[0,"rgb(5, 10, 172)"],[0.35,"rgb(40, 60, 190)"],[0.5,"rgb(70, 100, 245)"],\
            [0.6,"rgb(90, 120, 245)"],[0.7,"rgb(106, 137, 247)"],[1,"rgb(220, 220, 220)"]],
        autocolorscale = False,
        reversescale = True,
        marker = dict(
            line = dict (
                color = 'rgb(180,180,180)',
                width = 0.5
            ) ),
        colorbar = dict(
            autotick = False,
            title = 'Attack Range'),
      ) ]



fig = dict( data=data, layout=layout )

plot_url = plotly.offline.plot( fig, validate=False, filename='attack-year-2012.html' )