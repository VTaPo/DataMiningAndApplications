import getopt, sys
from utils import*

# list of command line arguments
argumentList = sys.argv[1:]

#short options
options ="hi:"

#long options
long_options=["help", "input="]

try:
	arguments, values = getopt.getopt(argumentList, options, long_options)

	if arguments[0][0] in ("-h", "--help"):
		basicHelpMessage()
	elif arguments[0][0] in ("-i", "--input"):
		num_missing_rows=0
		data=readDataset(str(arguments[0][1]))
		columns= getColumns(data)
		for i in range(getNumberOfSamples(data)):
			for c in columns:
				if isNull(data[c][i]):
					num_missing_rows+=1
					break
		print('The number of rows that have missing values: ', num_missing_rows)
except:
	showNotice()

