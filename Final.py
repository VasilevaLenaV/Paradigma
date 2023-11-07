def binary_search(search_arr, val):
    l_index = 0
    r_index = len(search_arr) - 1

    while l_index <= r_index:
        search_index = (l_index + r_index)

        if search_arr[search_index] == val:
            return search_index
        elif search_arr[search_index] < val:
            l_index = search_index + 1
        else:
            r_index = search_index - 1

    return -1


arr = [1, 3, 5, 8, 12, 20]
search_value = 5

print(binary_search(arr, search_value))
