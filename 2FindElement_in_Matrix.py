def search(self,matrix, n, m, x): 
    # code here 
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j]==x:
                return 1
    return 0
    