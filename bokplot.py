from bokeh.plotting import figure, output_file, show, reset_output
from bokeh.layouts import column
import numpy as np
import pandas as pd

import os

def plotIt( x_axi, wholedata, trainPredict, testPredict, startpoint, test_num, inx=0, title='plot' ):

	if not os.path.isdir( 'plot' ):
		os.mkdir( 'plot' )

	output_file( 'plot/' + str(inx ) + '.html' )

	p = figure(title=inx, x_axis_label='Time', y_axis_label='Load', x_axis_type="datetime", plot_width=1200)
	p.line( x_axi, wholedata[:,0] )

	startpoint = 24*6 + 1
	test_start = len( trainPredict ) + startpoint*2
	p.line( x_axi[ startpoint : startpoint+len( trainPredict ) ], trainPredict[:,0], color="#B3DE69" )
	p.line( x_axi[ test_start : test_start+len( testPredict ) ], testPredict[:,0], color="#CAB2D6" )

	show(p)
	
	reset_output()
	
def plot_comp( x_axi, wholedata, trainPredict, trainPredict_2, testPredict, 
	startpoint, test_num, title='plot', path=None, filename='plot' ):

	the_dir = 'plot' if path == None else str(path)

	os.mkdir( the_dir ) if not os.path.isdir(the_dir) else None

	output_file( the_dir + '/' + str( filename ) + '.html' )
	
	p = figure(title=title, x_axis_label='Time', y_axis_label='Load', x_axis_type="datetime", plot_width=1200)
	p.line( x_axi, wholedata[:,0] )

	test_pred_start = test_num[0] + startpoint
	train_2_start = test_num[1]+startpoint
	
	if trainPredict.shape[ -1 ] == 1:
		p.line( x_axi[ startpoint : startpoint+len( trainPredict ) ], trainPredict[:,0], color="#B3DE69" )
		p.line( x_axi[ test_pred_start : test_pred_start+len( testPredict ) ], testPredict[:,0], color="#CAB2D6" )
		p.line( x_axi[ train_2_start : train_2_start+len( trainPredict_2 ) ], trainPredict_2[:,0], color="#B3DE69" )
	else:
		p.line( x_axi[ startpoint : startpoint+len( trainPredict ) ], trainPredict, color="#B3DE69" )
		p.line( x_axi[ test_pred_start : test_pred_start+len( testPredict ) ], testPredict, color="#CAB2D6" )
		p.line( x_axi[ train_2_start : train_2_start+len( trainPredict_2 ) ], trainPredict_2, color="#B3DE69" )
		
	show(p)
	reset_output()

def plot_comp_ave( x_axi, wholedata, trainPredict, trainPredict_2, testPredict, 
	startpoint, test_num, ave_len, title='plot', path=None, filename='plot' ):

	the_dir = 'plot' if path == None else str(path)

	os.mkdir( the_dir ) if not os.path.isdir(the_dir) else None

	output_file( the_dir + '/' + str( filename ) + '.html' )
	
	p = figure(title=title, x_axis_label='Time', y_axis_label='Load', x_axis_type="datetime", plot_width=1200)
	p.line( x_axi[ : -ave_len+1 ], wholedata[:,0] )

	test_pred_start = test_num[0] + startpoint
	train_2_start = test_num[1] + startpoint

	if trainPredict.shape[ -1 ] == 1:
		p.line( x_axi[ startpoint : startpoint+len( trainPredict ) ], trainPredict[:,0], color="#B3DE69" )
		p.line( x_axi[ test_pred_start : test_pred_start+len( testPredict ) ], testPredict[:,0], color="#CAB2D6" )
		p.line( x_axi[ train_2_start : train_2_start+len( trainPredict_2 ) ], trainPredict_2[:,0], color="#B3DE69" )
	else:
		p.line( x_axi[ startpoint : startpoint+len( trainPredict ) ], trainPredict, color="#B3DE69" )
		p.line( x_axi[ test_pred_start : test_pred_start+len( testPredict ) ], testPredict, color="#CAB2D6" )
		p.line( x_axi[ train_2_start : train_2_start+len( trainPredict_2 ) ], trainPredict_2, color="#B3DE69" )

	show(p)
	reset_output()
	
def plot_score( trainScore, TestScore, path=None, filename='plot', title='plot' ):
	
	output_file( path + '/' + str( filename ) + '.html' )
	
	x_L = list( range( len( trainScore ) ) )
	
	p = figure(title=title, x_axis_label='time', y_axis_label='score', plot_width=1200)
	p.line( x_L, trainScore, color='#B3DE69', legend='train score' )
	p.line( x_L, TestScore, color='#CAB2D6', legend='test score' )
	p.legend.location = 'bottom_left'
	
	show(p)
	reset_output()
	