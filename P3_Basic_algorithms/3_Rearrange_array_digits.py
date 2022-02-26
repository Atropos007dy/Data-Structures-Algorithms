def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    def sort_one_bit(arr,left,right):
        left_index=left
        pivot_index=right
        pivot_value=arr[right]
        
        while pivot_index!=left_index:
            element=arr[left_index]
            if element<pivot_value:
                arr[left_index]=arr[pivot_index-1]
                arr[pivot_index-1]=pivot_value
                arr[pivot_index]=element
                pivot_index-=1
            else:
                left_index+=1
                
        return pivot_index
        
    def sort_all(arr,left,right):
        if left>=right:
            return
        pivot_index=sort_one_bit(arr,left,right)
        sort_all(arr, left, pivot_index - 1)
        sort_all(arr, pivot_index + 1, right)
        
    if not input_list:
        return
                
    for item in input_list:
        if item>9 or item<0:
            print('Invalid inputs')
            return
    
        
    
    N=len(input_list)
    if N==1:
        return input_list+[0]
    # sort the input:
    # use quick sort
    sort_all(input_list,0,len(input_list)-1)
    first_num=0
    second_num=0
    for ii in range(N):
        if ii%2==0:
            first_num=first_num*10+input_list[ii]
        else:
            second_num=second_num*10+input_list[ii]
    
    return [first_num,second_num]
    
    
    
    
        

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if not output:
        if not solution:
            print("output:{:},solution:{:}, Pass".format(output,solution))
        else:
            print("output:{:},solution:{:}, Fail".format(output,solution))
    
    elif sum(output) == sum(solution):
        print("output:{:},solution:{:}, Pass".format(output,solution))
    else:
        print("output:{:},solution:{:}, Fail".format(output,solution))


print('Test 1:')
test_function([[], None])
print('Test 2:')
test_function([[9], [9,0]])
print('Test 3:')
test_function([[89], None])
print('Test 4:')
test_function([[0,2,3,5,-2], None])
print('Test 5:')
test_function([[1, 2, 3, 4, 5], [542, 31]])
print('Test 6:')
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])
