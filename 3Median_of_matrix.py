def median(self, matrix, R, C):
    	#code here 
    lis=[]

    for i in range(R):

        lis+=matrix[i]

    lis.sort()

    return lis[len(lis)//2]