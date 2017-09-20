import pandas as pd
import os
import sys

format_book = {

	'krb' : {
		'folder_name' : 'krb',
		'to' : 'krb_floors',
		'files' : [
			'krb_jan.csv',
			'krb_feb.csv',
			'krb_mar.csv',
			'krb_april.csv',
			'krb_may.csv'
		]
	},
	
	'hq' : {
		'folder_name' : 'hq',
		'to' : 'hq_floors',
		'files' : [
			'hq_jan.csv',
			'hq_feb.csv',
			'hq_mar.csv',
			'hq_april.csv',
			'hq_may.csv'
		]
	}

}

instru = sys.argv[ 1 ]

book = format_book[ instru ]

folder_name = book[ 'folder_name' ]

files = [ folder_name + '/' + i for i in book[ 'files' ] ]

data_path = book[ 'to' ]

if not os.path.isdir( data_path ):
	os.mkdir( data_path )

for f in files:
	print( f )
	pd_data = pd.read_csv( f )
	
	inx = 0

	floors = set()
	
	while pd_data['location'][inx] not in floors:
		loc = pd_data['location'][inx]
		print( loc )
		new_frame = pd_data[ pd_data['location'] == loc ]
		
		file_name = '{}/{}.csv'.format( data_path, loc.replace( '/', '' ) )

		if os.path.isfile( file_name ):
			new_frame.to_csv( path_or_buf=file_name, mode='a', header=False, index=False )
		else:
			new_frame.to_csv( path_or_buf=file_name, mode='w', index=False )

		floors.add( loc )
		inx += 1

