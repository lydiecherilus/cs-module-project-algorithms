'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    index = 0
      
    # Traverse the array. replace each element non-zero elemnent at index 
    # increment index
    for i in range(len(arr)): 
        if arr[i] != 0: 
            arr[index] = arr[i] 
            index += 1
      
    # Make all elements 0 from index to end. 
    while index < len(arr): 
        arr[index] = 0
        index += 1
    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")