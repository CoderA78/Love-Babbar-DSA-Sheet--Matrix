def spirallyTraverse(self,matrix, r, c): 
    # code here 
    # code here 
    top, down = 0, r - 1
    left, right = 0, c - 1
    dir = 0
    result = []
    while top <= down and left <= right :
        if dir == 0:
            for r in range(left,right+1) :
                result.append(matrix[top][r])
            top += 1
        elif dir == 1 :
            for d in range(top,down+1) :
                result.append(matrix[d][right])
            right -= 1
        elif dir == 2 :
            for l in range(right,left-1,-1) :
                result.append(matrix[down][l])
            down -= 1
        else :
            for u in range(down,top-1,-1) :
                result.append(matrix[u][left])
            left += 1
        dir = (dir + 1)%4
    return result