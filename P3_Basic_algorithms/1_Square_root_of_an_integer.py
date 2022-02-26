def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if number<0:
        return 
    left=0
    right=number
    while left<=right:
        mid=left+(right-left)//2
        if mid**2==number:
            return mid
        elif mid**2<number:
            left=left+1
        else:
            right=right-1
    return right
            
        
print ("Pass" if  (None == sqrt(-1)) else "Fail")
print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")
print ("Pass" if  (29 == sqrt(888)) else "Fail")