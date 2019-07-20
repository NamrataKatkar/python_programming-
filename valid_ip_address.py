def valid_ipv4(ip):
	l=ip.split('.')
	if len(l)!= 4:
		return False
	for i in l:
		if not i.isnumeric():
			return False
		if int(i)<0 or int(i)>256:
			return False
	return True
  
if __name__=='__main__':
  ip='193.0.0.256'
  print(valid_ipv4(ip))
