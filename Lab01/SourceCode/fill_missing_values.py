import getopt, sys
import csv
from utils import*

input_=""
method='mean'
all=True
column=""
output="filled_file.csv"
# list of command line arguments
argumentList = sys.argv[1:]

#short options
options ="hi:m:c:o:a:"

#long options
long_options=["help", "input=","method=","column=","output=","all="]

#try:
arguments, values = getopt.getopt(argumentList, options, long_options)

if arguments[0][0] in ("-h", "--help"):
	helpMessageForFillMissingFunctions()
else:
	for i in range(len(arguments)):
		if arguments[i][0] in ("-i", "--input"):
			input_=str(arguments[i][1])
		elif arguments[i][0] in ("-m", "--method"):
			method = arguments[i][1]
		elif arguments[i][0] in ("-c", "--column"):
			column = arguments[i][1]
		elif arguments[i][0] in ("-o", "--output"):
			output=str(arguments[i][1])
		elif arguments[i][0] in ("-a", "--all"):
			all = arguments[i][1]

	outputFile=open(output,'w',newline='')
	writer=csv.writer(outputFile)

	data=readDataset(input_) #for DataFrame Structure to use functions in utils.py
	num_of_samples=getNumberOfSamples(data)

	titles=getColumns(data)
	writer.writerow(titles) #write columns name
	
	if all=="false" and checkMethod(method,column,data)==True:
		filledcol=fill_missing_valueOfCol(column, data, method)
		row=[]
		for i in range (num_of_samples):
			for j in range (len(titles)):
				row.append(data[titles[j]][i])
			# Change filled value
			index=findIndexOfCol(column,data)
			row[index]=filledcol[i]
			writer.writerow(row)
			for i in range (len(row)):
				del(row[0])
	elif all=="true":
		list_missing_columns=[] #saves missing columns
		type_missing_columns=[] #saves type of these missing columns
		index_missing_columns=[] #saves index of these missing columns in tittles
		filled_list=[] #saves these filled columns

		# Code to find list_missing_columns:
		for col in getColumns(data):
			if isNullList(list(data[col])):
				list_missing_columns.append(col)			
		# Code to find type of these missing columns:
		for i in range (len(list_missing_columns)):
			type_missing_columns.append(typeOfAttribute(list_missing_columns[i],data))
		# Code to find index of these missing columns in titles
		for j in range (len(list_missing_columns)):
			for k in range (len(titles)):
				if titles[k]==list_missing_columns[j]:
					index_missing_columns.append(k)
		# Code to fill these missing columns:
		for i in range (len(type_missing_columns)):
			if type_missing_columns[i]=='categorical':
				filled_list.append(fill_missing_valueOfCol(list_missing_columns[i],data,'mode'))
			elif type_missing_columns[i]=='numeric':
				filled_list.append(fill_missing_valueOfCol(list_missing_columns[i],data,method))
		
		# Code to write csv
		row=[]
		for i in range (num_of_samples):
			for j in range (len(titles)):
				row.append(data[titles[j]][i])
			# Change filled values
			for k in range (len(index_missing_columns)):
				row[index_missing_columns[k]]=filled_list[k][i]
			writer.writerow(row)
			# Del row[]
			for i in range (len(row)):
				del(row[0])

	print('Filling missing values done, checking in ', output)
	outputFile.close()
#except:
	#showNotice()
