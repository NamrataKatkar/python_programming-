/* Leet code - easy
Given a valid (IPv4) IP address, return a defanged version of that IP address.

A defanged IP address replaces every period "." with "[.]".

 

Example 1:

Input: address = "1.1.1.1"
Output: "1[.]1[.]1[.]1"
Example 2:

Input: address = "255.100.50.0"
Output: "255[.]100[.]50[.]0"
 

Constraints:

The given address is a valid IPv4 address.
*/


class Solution:
    def isvalid_ip(self,inp):
        l=inp.split('.')
        if len(l)!=4:
            return False
        for i in l:
            if not i.isnumeric():
                return False
            i=int(i)
            if i <0 or i >256:
                return False
        return True
    
    def defangIPaddr(self, address: str) -> str:
        valid= self.isvalid_ip(address)
        if valid:
            return address.replace('.','[.]')
        
