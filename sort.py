def selection_sort(alist):
    for i in range(0,len(alist)-1):
        smallest=i
        for j in range(i+1,len(alist)):
            if alist[j]<alist[smallest]:
                smallest=j
     alist[i],alist[smallest]=alist[smallest],alist[i]           
alist=input("Enter the list of number").split()
alist=(int(x)for x in alist)
selection_sort(a_list)
print('sorted list:',end='')
print(alist)
     
            
