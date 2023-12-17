'''
assuming that 'arr' is a 2D matrix size m*n
'''
def arrange(arr):
    top_bound = left_bound = 0
    bottom_bound = len(arr)-1
    right_bound = len(arr[0])-1
    size = len(arr[0])*len(arr)
    row = col = count = 0
    out = []

    while len(out) < size:
        while row <= right_bound and len(out) < size: #read right 
            out.append(arr[col][row])
            row+=1
        top_bound +=1
        row -=1
        col +=1

        while col <= bottom_bound and len(out) < size: #read down
            out.append(arr[col][row])
            col+=1
        right_bound-=1
        col -=1
        row -=1

        while row >= left_bound and len(out) < size: #read left
            out.append(arr[col][row])
            row-=1
        bottom_bound -=1
        col -=1
        row +=1

        while col >= top_bound and len(out) < size: #read up
            out.append(arr[col][row])
            col-=1
        left_bound+=1 
        col+=1
        row+=1

    return out

tests = [
[[1,2,3],[4,5,6],[7,8,9]], 
[[1,2,3],[8,9,4],[7,6,5]],
[[1,2],[3,4],[4,6],[7,8]],
[[1,2,3,4],[5,6,7,8],[9,10,11,12]],
[[1,2,3,4,5,6]],
[[1],[2],[3],[4],[5],[6]],
[[],[]]
]

answers = [
[1, 2, 3, 6, 9, 8, 7, 4, 5],
[1, 2, 3, 4, 5, 6, 7, 8, 9],
[1, 2, 4, 6, 8, 7, 4, 3],
[1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7],
[1, 2, 3, 4, 5, 6],
[1, 2, 3, 4, 5, 6],
[]
]

for i in range(len(tests)):
    out = arrange(tests[i])
    print( out == answers[i], out )