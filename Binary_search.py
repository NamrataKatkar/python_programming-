/*Given a sorted (in ascending order) integer array nums of n elements and a target value,
write a function to search target in nums. If target exists, then return its index, otherwise return -1.

Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
 

Note:

You may assume that all elements in nums are unique.
n will be in the range [1, 10000].
The value of each element in nums will be in the range [-9999, 9999].

*/

def bsearch(a,low,high,target):
    if len(a)==1 and a[high]==target:
        return 0
    if high>=1:
        m=(low+high)//2
        if a[m]<target:
            return bsearch(a,m+1,high,target)
        if a[m]>target:
            return bsearch(a,low,m-1,target)
        if a[m]==target:
            return m
    return -1
        
 if __name__='__main__':
    a=[-1, 0, 3, 5, 9, 12]
    low=0
    high=len(a)-1
    target=3
    print(bsearch(a,low,high,target))
