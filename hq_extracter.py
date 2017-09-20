import pandas as pd
ifiles=['sjs_all_feb_report_m.csv']
floors=['HQ - G/F'
,'HQ - 2S'
,'HQ - 2N'
,'HQ - 3S'
,'HQ - 3N'
,'HQ - 4N'
,'HQ - 5S'
,'HQ - 5N'
,'HQ - 6S'
,'HQ - 6N'
,'HQ - 7S'
,'HQ - 7N'
,'HQ - 8S'
,'HQ - 8N'
,'HQ - 9S'
,'HQ - 9N'
,'HQ - AC'
,'HQ - 11'
,'HQ - 12'
,'HQ - 13'
,'HQ - Lift'
,'HQ - 10']

def extract_hq(file):
	print("here")
	df=pd.read_csv(file)
	hq_df=pd.DataFrame()
	floor=[]
	for f in floors:
		floor.append(df[df['location']==f])
	hq_df=pd.concat(floor)
	print(hq_df.head())
	hq_df.to_csv('hq_jan.csv')

def main():
	for file in ifiles:
		extract_hq(file)

if __name__=='__main__' :
	print("ok")
	main()