import pandas as pd

temp_file_names = [ 
	'temperatures_jan.csv',
	'temperatures_mar.csv',
	'temperatures_may.csv'
]

pd.concat( [ pd.read_csv(f) for f in temp_file_names ], ignore_index = True ).to_csv('all_temp.csv', index=False)

humid_file_names = [ 
	'humidities_jan.csv',
	'humidities_mar.csv',
	'humidities_may.csv'
]

pd.concat( [ pd.read_csv(f) for f in humid_file_names ], ignore_index = True ).to_csv('all_humid.csv', index=False)
