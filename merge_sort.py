def merge(arr):
    if(len(arr) > 1):
        mid = len(arr) // 2

        left_arr = arr[:mid]
        right_arr = arr[mid:]

        merge(left_arr)
        merge(right_arr)

        l_index = r_index = arr_index = 0

        while((l_index < len(left_arr)) and (r_index < len(right_arr))):
            if(left_arr[l_index] <= right_arr[r_index]):
                arr[arr_index] = left_arr[l_index]
                l_index += 1
            else:
                arr[arr_index] = right_arr[r_index]
                r_index += 1
            arr_index += 1

        # Check if any items are left in left array
        while l_index < len(left_arr):
            arr[arr_index] = left_arr[l_index]
            arr_index += 1
            l_index += 1

        # Check if any items are left in right array
        while r_index < len(right_arr):
            arr[arr_index] = right_arr[r_index]
            arr_index += 1
            r_index += 1


array = [5, 2, 4, 6, 1, 3]

merge(array)
print(array)
