import pandas as pd
from os import listdir


def clean_wx_data():
	"""Grabs all .csv files in a directory & aggregates based on date"""
	suffix = ".csv"
	filenames = listdir()
	files = [f for f in filenames if f.endswith(suffix)]

	if len(files) == 1:
	    d = pd.read_csv(files[0], parse_dates=['DATE'], low_memory=False)
	    d = d[['DATE', 'AWND', 'PRCP', 'TAVG', 'TMAX', 'TMIN']]
	# else:
	#     d = pd.concat([pd.read_csv(f, index_col=0, header=None, axis=1) for f in files], keys=files)
	#     d = d[['DATE', 'AWND', 'PRCP', 'TAVG', 'TMAX', 'TMIN']]

	new_df = d.groupby(['DATE'], as_index=False).mean()
	new_df.to_csv('agg_wx_data.csv', index=False)


if __name__ == "__main__":
	clean_wx_data()