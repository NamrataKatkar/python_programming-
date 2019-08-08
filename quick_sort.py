# this quick_sort uses last index as pivot
def partition(a,low,high):
    i=low-1
    pivot=a[high]
    for j in range(low,high):
        if a[j]<=pivot:
            i+=1
            a[j],a[i]=a[i],a[j]
    a[i+1],a[high]=a[high],a[i+1]
    return i+1
            
def quicksort(a,low,high):
    if low<high:
        pi=partition(a,low,high)
        quicksort(a,low,pi-1)
        quicksort(a,pi+1,high)
   
if __name__=='__main__':
    a=[45,32,5,0,2,67,4,34,65]
    n=len(a)
    quicksort(a,0,n-1)
    print(a)
