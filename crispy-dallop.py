'''
12 = 21
513 = 531
2017 = 2071
9 = -1
111 = -1
531 = -1
0 = -1
123 = 132
215430 = 230145
4321 = -1
[12,513,2017,9,111,531,0,123,215430,4321]
'''

# assuming that input 'num' is a positive integer
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
            out = ''.join([str(x) for x in num_arr])
            break

    return out


tests = [12,513,2017,9,111,531,0,123,215430,4321,000]
for test in tests:
    print(nextNumber(test))