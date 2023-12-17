'''
assuming that input 'num' is a positive integer
'''
def nextNumber(num):
    out = -1
    break_index = None

    if num <= 9: #num is a single digit
        return out

    num_arr = [int(x) for x in str(num)] #convert int to arr

    for i in range(len(num_arr)-1,0,-1):
        if num_arr[i] > num_arr[i-1]:
            break_index = i-1
            num_arr[break_index+1:] = sorted(num_arr[break_index+1:])
            for j in range(break_index+1, len(num_arr)):
                if num_arr[break_index] < num_arr[j]:
                    num_arr[j], num_arr[break_index] = num_arr[break_index],num_arr[j]
                    break
            out = int(''.join([str(x) for x in num_arr]))
            break

    return out


tests = [12,513,2017,9,111,531,0,123,215430,4321,000]
answers = [21,531,2071,-1,-1,-1,-1,132,230145,-1,-1,-1]
for i in range(len(tests)):
    out = nextNumber(tests[i])
    print( out == answers[i], out )
