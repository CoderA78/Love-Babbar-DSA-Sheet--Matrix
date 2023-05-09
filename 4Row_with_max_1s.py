def rowWithMax1s(self,arr, n, m):
    # code here
    l=[]
    for i in range(n):
        x=arr[i].count(1)
        l.append(x)
        
    x=max(l)
    if x==0:
        return -1
    else:
        return(l.index(max(l)))