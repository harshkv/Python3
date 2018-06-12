a = [23,345,43,12,6,6,12,45,5]
print(a)
def insertion_sort(a):
    for i in range(1,len(a)):
        key = a[i]
        j = i-1
        while(j>=0 and key < a[j]):
            a[j+1] = a[j]
            j -= 1
        a[j+1] = key
    print(a)
insertion_sort(a)
