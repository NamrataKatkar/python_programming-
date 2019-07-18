/* flatten the following dictionaryinto list
d = {
	'name': 'Steven',
	'children': [{
		'name': 'Jessica',
		'children': []
	}, {
		'name': 'George',
		'children': []
	}]
}

*/

def flatten_dictionary(d, op):
	for key,val in d.items():
		if key=='name':
			op.append(val)
		if key == 'children':
			for k in val:
				flatten_dictionary(k, op)
	return op
  
  if __name__=='__main__':
    d={'name': 'Steven', 'children': [{'name': 'Jessica', 'children': []}, {'name': 'George', 'children': []}]}
    output=[]
    print(flatten_dictionary(d,output))
