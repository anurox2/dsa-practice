def main(arr):
    arr_len = len(arr)

    # Improvement of insertion sort. LOL
    condition = False
    for index in range(0, arr_len):

        # Load the current item at index into key
        key = arr[index]

        # Load the previous item from index into prev_index
        prev_index = index - 1

        # Check if the previous item is greater than current item
        # Keep moving it backwards until the condition is reversed
        while((prev_index >= 0) & (arr[prev_index] > key)):
            print('hit')
            condition = True
            arr[prev_index+1] = arr[prev_index]
            prev_index -= 1

        # If the while loop isn't triggered don't trigger item overwrite
        if(condition):
            arr[prev_index + 1] = key
            condition = False

    return arr


# array = [5, 2, 4, 6, 1, 3, 1234, 21, 213, 4, 432, 29301, 2, 5]
# array = [1, 2, 2, 3, 4, 4, 5, 5, 6, 21, 213, 432, 1234, 29301]

array = [1, 2, 3, 4, 5, 6]

sorted_arr = main(array)
print('\n\n', sorted_arr, '\n\n')
