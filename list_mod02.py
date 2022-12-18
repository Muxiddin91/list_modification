def remove_even(lst):
    '''Given a list of numbers, write a function that returns a new list where all the even numbers are removed.
    
    Args:
        lst (list): list of numbers.
        
    Returns:
        list: list without even numbers.
    '''
    a = []
    for i in lst:
        if i%2==1:
            a.append(i)
    return a
print(remove_even([1,2,3,4,5,6,5,5,5,5,5,5,4,4,4,4]))