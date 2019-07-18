/* flatten the list of list . Time complexity = O(n*m), Space complexity = O (n*m) */
l=[[1, 2, 3], [4, 5, 6], [7], [8, 9]]
output=[]
for i in l:
	for j in i:
		output.append(j)
    
print(output)

