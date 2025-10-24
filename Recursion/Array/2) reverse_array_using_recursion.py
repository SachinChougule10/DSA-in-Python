def reverse_array(mylist, left, right):
    if left >= right:
        return mylist
    mylist[left], mylist[right] = mylist[right], mylist[left]
    return reverse_array(mylist, left + 1, right - 1)


my_list = [5, 9, 8, 3, 6, 7, 1, 4, 2]
print(reverse_array(my_list, 0, 8))
