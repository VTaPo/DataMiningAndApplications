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
		data=readDataset(str(arguments[0][1]))
		
		list_missing_columns=[]
		for col in getColumns(data):
			if isNullList(list(data[col])):
				list_missing_columns.append(col)

		print('List of missing columns:\n')
		for col in list_missing_columns:
			print(col)
		print('\nSum of missing columns: ',len(list_missing_columns))
except:
	showNotice()
