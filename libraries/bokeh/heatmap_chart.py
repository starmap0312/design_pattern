import pandas as pd

from bokeh.charts import HeatMap, bins, output_file, show
from bokeh.layouts import column, gridplot
from bokeh.palettes import RdYlGn6, RdYlGn9
from bokeh.sampledata.autompg import autompg
from bokeh.sampledata.unemployment1948 import data
# setup data sources
del data['Annual']
print(type(data))

data['Year'] = data['Year'].astype(str)
unempl = pd.melt(data, var_name='Month', value_name='Unemployment', id_vars=['Year'])

jobs = {'time_process': [20161104, 20161105, 20161106],
        'job_status': [0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1],
        'job_id': [72, 74, 4251, 4252, 4253]}
jobs['job_id'] = [str(id) for id in jobs['job_id']]

hmap = HeatMap(jobs, y='job_id', x='time_process', values='job_status', stat=None)

output_file("heatmap.html", title="heatmap.py example")

show(column(gridplot(hmap, ncols=2, plot_width=400, plot_height=400),))
