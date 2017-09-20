from bokeh.plotting import figure, output_file, show, reset_output
from bokeh.layouts import column
import numpy as np
import pandas as pd
import os

def plot_file( file, path, plot_dir ):

	dt = pd.read_csv( os.path.join( path, file ) )

	axis_datetime = np.array(dt['Time'], dtype=np.datetime64)

	col_list = list( i for i in dt.columns.values if i != 'Time' )

	if not os.path.isdir( plot_dir ):
		os.mkdir( plot_dir )

	full_path = os.path.join( plot_dir, file.split( '.' )[0] + '.html' )

	output_file( full_path )

	plot_list = []

	for c in col_list:
		p = figure(title=c, x_axis_label='Time', y_axis_label=c, x_axis_type="datetime", plot_width=1200)
		p.line( axis_datetime, dt[c] )
		plot_list.append( p )

	p = column( plot_list )

	show(p)

	reset_output()

if __name__ == '__main__':
	
	p = 'dataHour/hq'
	
	files = [ f for f in os.listdir( p ) if os.path.isfile( os.path.join( p, f) ) ]

	res = [ plot_file( f, p, 'plot_hq' ) for f in files ]
	
	p = 'dataHour/krb'
	
	files = [ f for f in os.listdir( p ) if os.path.isfile( os.path.join( p, f) ) ]

	res = [ plot_file( f, p, 'plot_krb' ) for f in files ]