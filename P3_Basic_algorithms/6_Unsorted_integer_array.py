def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if not ints:
        return (None,None)
    N=len(ints)
    if N==1:
        return (ints[0],ints[0])
        
    smallest=ints[0]
    largest=ints[0]
    for ii in range(1,N):
        item=ints[ii]
        if item>largest:
            largest=item
        if item<smallest:
            smallest=item
            
    return (smallest,largest)
            
    
        
            

## Example Test Case of Ten Integers
import random



print('Test 1:')
l = [3,2,1,9,0,4]
print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")

print('Test 2:')
l=[2,2,2,2,2]
print ("Pass" if ((2, 2) == get_min_max(l)) else "Fail")

print('Test 3:')
l=[2]
print ("Pass" if ((2, 2) == get_min_max(l)) else "Fail")

print('Test 4:')
l=[]
print ("Pass" if ((None, None) == get_min_max(l)) else "Fail")