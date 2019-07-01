*** find 3 elements from the list that have minimum difference with the given target value.***

def three_sum_diff(l,target):
    curr_val=0
    prev_val=float("inf")
    op=[]
    for i in range(0,len(l)-2):
        for j in range(i+1,len(l)-1):
            for k in range(j+1,len(l)):
                curr_val=abs(target - (l[i]+l[j]+l[k]))
                if curr_val<prev_val:
                    op=[]
                    op.append([l[i],l[j],l[k]])
                    prev_val=curr_val
    return op
   
if __name__=="__main__":
    l=[1,2,3,4,5,6,7,8]
    target=int(input("input th number : "))
    print(three_sum_diff(l,target))
