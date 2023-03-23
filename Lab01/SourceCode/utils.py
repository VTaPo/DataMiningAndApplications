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

def helpMessageForCalculateFunctions():
	print('========================================================================================')
	print('|| DATA PREPROCESSING:                                                                 ||')
	print('||                                                                                     ||')
	print('|| -h/--help to show instructions                                                      ||')
	print('|| -i/--input=... to input path to csv file                                            ||')
	print('|| -f/--first=... to input first column you want to calculate                          ||')
	print('|| -s/--second=... to input second column you want to calculate                        ||')
	print('|| -o/--output=... to output path to output file                                       ||')
	print('|| DEFAULT METHOD IS ADD, DEFAULT OUTPUT FILE PATH: "caculatation_result.csv"          ||')
	print('=========================================================================================')   

def helpMessageForFillMissingFunctions():
	print('========================================================================================')
	print('|| DATA PREPROCESSING:                                                                 ||')
	print('||                                                                                     ||')
	print('|| -h/--help to show instructions                                                      ||')
	print('|| -i/--input=... to input path to csv file                                            ||')
	print('|| -c/--column=... to input column you want to fill in                                 ||')
	print('|| -m/--method=...(mean/median/mode) to input method you want to use to fill in        ||')
	print('|| -a/--all=...(true/false) to input if you want to fill all missing columns or not    ||')
	print('|| -o/--output=... to output path to output file                                       ||')
	print('|| DEFAULT METHOD IS ADD, DEFAULT OUTPUT FILE PATH: "caculatation_result.csv"          ||')
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

# Cau 3
def typeOfAttribute(col,data):
    for i in range (getNumberOfSamples(data)):
        if isNull(data[col][i])==False:
            if type(data[col][i])==int or type(data[col][i])==np.int64 or type(data[col][i])==np.int32 or type(data[col][i])==float or type(data[col][i])==np.float64 or type(data[col][i])==np.float32:
                return 'numeric'
                break
            else:
                return 'categorical'
                break

def meanOfCol(col,data):
    sum=0
    sample=0
    for i in range (getNumberOfSamples(data)):
        if isNull(data[col][i])==False:
            sample=sample+1
            sum=sum+data[col][i]
    mean=sum/sample
    return mean

def freqOfValue(value,col,data):
    freq=0
    for i in range (getNumberOfSamples(data)):
        if data[col][i]==value:
            freq=freq+1
    return freq

def findMax(list_):
    maxValue=list_[0]
    for i in range (len(list_)):
        if list_[i]>maxValue:
            maxValue=list_[i]
    return maxValue
        
def modeOfCol(col,data):
    value=[] #Value of Index i
    freq=[]  #List saves freq of Value of Index i
    for i in range (getNumberOfSamples(data)):
        if isNull(data[col][i])==False and (data[col][i] in value)==False:
            value.append(data[col][i])
            freq.append(freqOfValue(data[col][i],col,data))
    maxFreq=findMax(freq)
    for i in range (len(freq)):
        if value[i]==maxFreq:
            index=i
    return value[i]
def medianOfCol(col,data):
    list_=[] #List saves not null values of this column
    for j in range (getNumberOfSamples(data)):
        if isNull(data[col][j])==False and (data[col][j] in list_)==False:
            list_.append(data[col][j])
    i=(len(list_)+1)/2
    list_.sort()
    if len(list_)%2!=0:
        return list_[i]
    else:
        return (list_[round(i)]+list_[round(i)-1])/2
    
def fill_missing_valueOfCol(col,data,methods):
    fill=list(data[col])
    if methods=='mean':
        x=meanOfCol(col,data)
        for i in range(getNumberOfSamples(data)):
            if isNull(fill[i]):
                fill[i]=x
    elif methods=='median':
        x=medianOfCol(col,data)
        for i in range(getNumberOfSamples(data)):
            if isNull(fill[i]):
                fill[i]=x
    else:
        x=modeOfCol(col,data)
        for i in range(getNumberOfSamples(data)):
            if isNull(fill[i]):
                fill[i]=x
    return fill

def findIndexOfCol(col,data):
     title=getColumns(data)
     for i in range(len(title)):
          if title[i]==col:
               return i

def checkMethod(method,col,data):
    if typeOfAttribute(col,data)=='numeric':
        if method=='mean' or method=='median':
            return True
        else: return False
    elif typeOfAttribute(col,data)=='categorical':
        if method=='mode':
             return True
        else:
             return False
    return False
       
#Cau 4
def add(numA,numB):
    if isNull(numA)==False and isNull(numB)==False:
        return numA+numB
    else:
        if isNull(numA)==True:
            return numA
        else:
            return numB
        
def sub(numA,numB):
    if isNull(numA)==False and isNull(numB)==False:
        return numA-numB
    else:
        if isNull(numA)==True:
            return numA
        else:
            return numB

def mul(numA,numB):
    if isNull(numA)==False and isNull(numB)==False:
        return numA*numB
    else:
        if isNull(numA)==True:
            return numA
        else:
            return numB
        
def div(numA,numB):
    if isNull(numA)==False and isNull(numB)==False:
        return numA/numB
    else:
        if isNull(numA)==True:
            return numA
        else:
            return numB