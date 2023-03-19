import pandas as pd 
import numpy as np

def readDataset(fileName):
	data=pd.read_csv(fileName)
	return data

def showNotice():
	print('Adding -h/--help for instructions')

def basicHelpMessage():
	print('==============================================')
	print('|| DATA PREPROCESSING:                      ||')
	print('||                                          ||')
	print('|| -h/--help to show instructions           ||')
	print('|| -i/--input=... to input path to csv file ||')
	print('==============================================')

def helpMessageForRemovingFunctions():
	print('========================================================================================')
	print('|| DATA PREPROCESSING:                                                                 ||')
	print('||                                                                                     ||')
	print('|| -h/--help to show instructions                                                      ||')
	print('|| -i/--input=... to input path to csv file                                            ||')
	print('|| -t/--threshold=... to input allowed threshold percentage of missing value           ||')
	print('|| -o/--output=... to output path to output file                                       ||')
	print('|| DEFAULT THRESHOLD IS 0%, DEFAULT OUTPUT FILE PATH: "output.csv"                     ||')
	print('=========================================================================================')

def getColumns(data):
	return list(data)

def getNumberOfAttributes(data):
	return len(getColumns(data))

def getNumberOfSamples(data):
	return len(data)

def isNull(number):
	return number!=number 

def isNullList(l):
	result=[isNull(value) for value in l]
	return True in result

def computePercentageOfMissingValuesInRow(data,row):
	sum_missing_values=0
	for c in getColumns(data):
		if isNull(data[c][row]):
			sum_missing_values+=1
	return (sum_missing_values/getNumberOfAttributes(data))*100

def computePercentageOfMissingValuesInColumn(data,column):
	sum_missing_values=0
	for i in range(getNumberOfSamples(data)):
		if isNull(data[column][i]):
			sum_missing_values+=1
	return (sum_missing_values/getNumberOfSamples(data))*100


