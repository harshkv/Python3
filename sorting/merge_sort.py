a = [213,43,23,6,321,5,65,2,6,7,8,2,1,6,458,0]
print(a)
def merge_sort(a):
    if(len(a)>1):
        mid = len(a)//2
        lefth = a[:mid]
        righth = a[mid:]
        merge_sort(lefth)
        merge_sort(righth)
        i = j = k = 0
        while( i < len(lefth) and j < (len(righth))):
            if(lefth[i] < righth[j]):
                a[k] = lefth[i]
                i +=1
            else:
                a[k] = righth[j]
                j +=1
            k+=1
        while( i < len(lefth)):
            a[k] = lefth[i]
            i +=1
            k += 1
        while( j< len(righth)):
            a[k] = righth[j]
            j +=1
            k +=1
merge_sort(a)
print(a)
        
        
        
           
    
    
