def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    next_pos_0=0
    next_pos_2=len(input_list)-1
    front_index=0
    #check invalid input:
    if set(input_list)!=set([0,1,2]):
        print('Invalid inputs, array must contain and only contain 0,1,2.')
        return
    
    while front_index <=next_pos_2:
        front=input_list[front_index]
        if front==0:
            input_list[front_index],input_list[next_pos_0]=input_list[next_pos_0],input_list[front_index]
            front_index+=1
            next_pos_0+=1
        elif front==2:
            input_list[front_index],input_list[next_pos_2]=input_list[next_pos_2],input_list[front_index]
            next_pos_2-=1
        else:
            front_index+=1       
    #print(input_list)
            
    return input_list

def test_function(test_case):
    #check invalide
    sorted_array = sort_012(test_case)
    #print(set(test_case))
    
    if set(test_case)!=set([0,1,2]):
        if not sorted_array:
            print("input: {:},sort_12: {:}, Pass".format(test_case,sorted_array))
        else:
            print("input: {:},sort_12: {:}, Fail".format(test_case,sorted_array))
    
    else:
        if sorted_array == sorted(test_case):
            print("sort_12: {:}, Pass".format(sorted_array))
        else:
            print("sort_12: {:}, Fail".format(sorted_array))

print('Test 1:')
test_function([0,1,3])
print('Test 2:')
test_function([2,2,2])
print('Test 3:')
test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
print('Test 4:')
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
print('Test 5:')
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
print('Test 6:')
test_function([2,2,1,1,0])
print('Test 7:')
test_function([])




