def shell_sort(array):
    length = len(array)
    gap = length // 2
    while gap > 0:
        for i in range(gap, length):
            temp = array[i]
            j = i
            while j >= gap and array[j - gap] > temp:
                array[j] = array[j - gap]
                j -= gap
            array[j] = temp
        gap //= 2

    return  array

my_list = [2, 4, 8, 1, 6, 7, 9, 3, 5, 0]
sorted_list = shell_sort(my_list)
print(f"Отсортированный список: {sorted_list}")