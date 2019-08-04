/* Print all possible strings of length k that can be formed from a set of n characters
Given a set of characters and a positive integer k, print all possible strings of length k that can be formed from the given set.
Examples:

Input: 
set[] = {'a', 'b'}, k = 3

Output:
aaa
aab
aba
abb
baa
bab
bba
bbb


Input: 
set[] = {'a', 'b', 'c', 'd'}, k = 1
Output:
a
b
c
d

Solution:
*/
def fun(set,prefix,k,n):
	if k==0:
		print(prefix)
		return
	else:
		for i in set:
			newprefix=prefix+i
			fun(set,newprefix,k-1,n)

if __name__=='__main__':
	set=['a','b']
	k=3
	n=len(set)
	fun(set,'',k,n)
