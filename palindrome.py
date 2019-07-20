/* Approach 1 (using string slicing) */
def isPalindrome(s):
	s=str(s)
	if s[:]==s[::-1]:
		return True
	else:
		return False
    
if __name__=='__main__':
	a='geeg'
	print("String is palindrome ? " + str(isPalindrome(a)))


/* Approach 2 without using inbuilt function  */
def isPalindrome(s):
	n=len(s)
	for i in range(0,n//2):
		if a[i]!=a[n-1-i]:
			return False
	return True
	
if __name__=='__main__':
	a='malayalam'
	print("String is palindrome ? " + str(isPalindrome(a)))

	
	
