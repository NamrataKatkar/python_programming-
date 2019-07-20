/* The atoi() function converts a character string to an integer value. */
def atoi(s):
  res=0
	if not s.isnumeric():
		return -1
	else:
		for i in s:
			res=res*10+int(i)
		return res
    
 if __name__=='__main__':
	print(atoi('2324324324'))
	print(atoi('sgdfjdf'))
