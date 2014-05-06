import re
import MySQLdb
import json
import re
group = {}
summaryOutput = "summary.txt"
output = open(summaryOutput,'w')


def main():
	global group,summaryOutput,output
	summary("country.txt")
	summary("428/newData-hj-428.txt")
	summary("428/newData-jx-428.txt")
	summary("428/newData--ZJ4-28.txt")
	summary("429/newData--hj.txt")
	summary("429/newData-jx.txt")
	summary("429/newData--zz.txt")
	summary("430/newData-hj.txt")
	summary("430/newData-jx.txt")
	summary("430/newData-xx.txt")
	summary("430/newData--zj.txt")
	summary("504/newData--HJ5-4.txt")
	summary("504/newData--xx-5-4.txt")
	summary("504/newData--ZJ5-4.txt")
	summary("505/newData-xx-5-5.txt")
	summary("505/newData--ZJ5-5.txt")
	#print group
	group = sorted(group.iteritems(),key= lambda d:d[0],reverse= False)
	for key in group:
		print key[0]
		output.write(re.sub('\n','',str(key[0]))+'#')
		for keyword in  key[1]:
			print keyword
			output.write(str(re.sub('\n','',keyword))	+'#')
		print "\n--------------"
		output.write('\n')
	
def summary(fileName):
	global group
	file = open(fileName,'r');
	while True:
		element = file.readline();
		if not element: break
		analyze(element)
		
		
		
def analyze(element):
	global group
	element = re.sub('\n','',element)
	arr = element.split('#')	
	#print arr
	#print arr[0]

	if group.has_key(re.sub('\n','',arr[0])):
		if len(arr) == 1:
			return
		for i in range(1,len(arr)-1):
	#		print arr[i]
			if group[arr[0]].has_key(re.sub('\n','',arr[i])):
				group[arr[0]][re.sub('\n','',arr[i])] = group[arr[0]][re.sub('\n','',arr[i])] +1
			else:
				group[arr[0]][re.sub('\n','',arr[i])] = 1
	else:
		group[arr[0]] = {}
		if len(arr) == 1:
			return
		#print arr[1]
		if len(arr) == 2:
			if group[arr[0]].has_key(re.sub('\n','',arr[1])):
				group[arr[0]][re.sub('\n','',arr[1])] = group[arr[0]][re.sub('\n','',arr[1])] +1
			else:
				group[arr[0]][re.sub('\n','',arr[1])] = 1
		for i in range(1,len(arr)-1):
			if group[arr[0]].has_key(re.sub('\n','',arr[i])):
				group[arr[0]][re.sub('\n','',arr[i])] = group[arr[0]][re.sub('\n','',arr[i])] +1
			else:
				group[arr[0]][re.sub('\n','',arr[i])] = 1
	

main()