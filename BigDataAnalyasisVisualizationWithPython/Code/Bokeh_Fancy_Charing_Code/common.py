# replace output_file as notebook
from bokeh.plotting import figure, show, output_file, output_notebook
from bokeh.charts import output_file

def output_file2(*args, **kwargs):
    output_notebook()

import sys
sys.modules['bokeh.plotting'].output_file = output_file2
sys.modules['bokeh.charts'].output_file = output_file2