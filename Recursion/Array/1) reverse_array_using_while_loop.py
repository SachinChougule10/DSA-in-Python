def reverse_array(my_list):
    left = 0
    right = len(my_list) - 1

    while left < right:
        my_list[left], my_list[right] = my_list[right], my_list[left]
        left += 1
        right -= 1
    return my_list


my_list = [5, 9, 8, 3, 6, 7, 1, 4, 2]
print(reverse_array(my_list))
