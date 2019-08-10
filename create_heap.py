def max_heapify(a,i,n):
    l=2*i + 1
    r=2*i + 2
    largest=i
    if l<n and a[l]>a[largest]:
        largest=l
    if r<n and a[r]>a[largest]:
        largest=r
    if i!=largest:
        a[i],a[largest]=a[largest],a[i]
        max_heapify(a,largest,n)
        
def min_heapify(a,i,n):
    l=2*i + 1
    r=2*i + 2
    smallest=i
    if l<n and a[l]<a[smallest]:
        smallest=l
    if r<n and a[r]<a[smallest]:
        smallest=r
    if i!=smallest:
        a[i],a[smallest]=a[smallest],a[i]
        min_heapify(a,smallest,n)

if __name__=='__main__':
    a=[7,600,90,100,5]
    n=len(a)
    index=(n//2)-1
    print('arr :' ,a)
    for j in range(index,-1,-1):
        max_heapify(a,j,n)
    print('max heap :' ,a)
    b=[7,600,90,100,5]
    print('arr :' ,b)
    for j in range(index,-1,-1): 
        min_heapify(b,j,n)
    print('max heap :' ,b)
