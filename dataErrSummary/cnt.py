import re
def main():
	fileName = "country.txt"
	file  = open(fileName)
	paper_id = 1
	while True:
		#print "hello"
  		element = file.readline()
  		#print element
  		if not element: break
  		try:
  			data = element.split('#')
  			print data[0]
  			#print group
  		except SyntaxError, e : 
  			print "error"
  			print e
  		except KeyError, e:
  			print "key error"
  			print e
  		except NameError, e :
  			print "Name error"
  			print e
  			nameError = nameError + 1
  		paper_id = paper_id+1
	file.close()
main()
