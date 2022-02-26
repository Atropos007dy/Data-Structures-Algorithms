def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    if not input_list:
        return -1
    left=0
    right=len(input_list)-1
    while left<=right:
        mid=left+(right-left)//2
        if input_list[mid]==number:
            return mid
        elif input_list[mid]>=input_list[left]:
            if number>=input_list[left] and number<input_list[mid]:
                right=mid-1
            else:
                left=mid+1
        else: #input_list[mid]<input_list[left]
            if number>input_list[mid] and number <=input_list[right]:
                left=mid+1
            else:
                right=mid-1
                
    return -1
   

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    l=linear_search(input_list, number)
    r=rotated_array_search(input_list, number)
    if l== r:
        print("linear search return: {:}, binary search return: {:}, Pass".format(l,r))
    else:
        print("linear search return: {:}, binary search return: {:},Fail".format(l,r))

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], -999]) 
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 2])
test_function([[6, 7, 8, 1, 2, 3, 4], 7])
test_function([[6], None])
test_function([[], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 999])