import re
import MySQLdb
import json
import re


def main():
	fileName = 'pnasErrData'
	hello(fileName)
	fileName = 'sciErrData'
	hello(fileName)
	fileName = 'natErrData'
	hello(fileName)
def hello(fileName):
	file = open('429/'+fileName+'.txt','r');
	output = open("430/"+fileName+'New.txt','w');
	group={}
	while True:
		element = file.readline();
		if not element: break
		group = analyze(group,element)
		
	for key in group:
		print key
		output.write(str(key)+'\n')
		
		
def analyze(group,element):
	if group.has_key(element):
		group[element] = group[element]+1
	else:
		group[element] = 1
	country = showCountry(element)
	if country != '':
		del group[element]
	return group

def showCountry(key):
	Datafile={}
	Datafile[0]= '430/newData-hj.txt'
	Datafile[1]= '430/newData-jx.txt'
	Datafile[2]= '430/newData-xx.txt'
	Datafile[3]='430/newData--zj.txt'

	
	for dataKey in Datafile:
		countryFile = open(Datafile[dataKey],'r')
		while True:
			i=0
			element = countryFile.readline()
	  		if not element: break
	  		#print element
	  		Info = element.split('#')
	  		if len(Info) == 1:
	  			continue
	  		for keyword in Info:
	  			if keyword == '' or keyword == '\n' or keyword == ' ' or keyword == '\t':
	  				continue
	  			#print i
	  			try:
	  				country = re.search(keyword,key)
	  				if country is not None:
	  					print str(i)+'the file is '+str(dataKey)
	  					print Info[0]+'\t the key word is '+keyword+'\t@'+key
	  					return Info[0]
	  			except TypeError:
	  				'''
	  				print keyword
	  				print key
	  				print i
	  				'''
	  	countryFile.close()
  	return ''
main()