def linear_search(arr, target):
    # loop thru the length of the array
    for i in range(len(arr)):
       # if i is in array then return it.
       if arr[i] == target:
           return i

    
    return -1 # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here
    # left is the starting point
    left = 0
    # right is the very last index in array
    right = len(arr) -1

    # find the middle || if the left is greater than or equal to the right.
    while left <= right:
        # then add the L & R and divde by 2
        middle = (left + right) // 2

        # check if middle is the target. 
        if arr[middle] == target:
            return middle
        else:
            # if target is greater than the number in the middle index
            if target < arr[middle]:
                # -1 from right until we get to middle. 
                right = middle -1
            else:
                # if not add +1 to the left until we get to middle
                left = middle +1


    return -1  # not found
