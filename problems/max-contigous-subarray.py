def max_sum(arr):
    max_prev = arr[0]
    max_curr = arr[0]

    for number in range(1, len(arr)):
        max_prev = max(arr[number], (max_prev + arr[number]))
        max_curr = max(max_curr, max_prev)

    return max_curr


array = [13, -3, -25, 20, -3, -16, -23, 1,
         18, 20, -7, 12, 7, -5, -22, 15, -4, 7]

print(max_sum(array))
