def selection_sort(a):
    for i in range(0,len(a)-1):
        current_min = i
        for j in range(i+1,len(a)):
            if a[j]<a[current_min]:
                current_min=j
        if current_min != i:
            temp=a[i]
            a[i]=a[current_min]
            a[current_min]=temp        
    return a
    
  if __name__="__main__":
    a=[2,15,9,88,1]
    print(selection_sort(a))
