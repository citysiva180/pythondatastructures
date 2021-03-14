# Here we would be working with selection sort.
def selectionSort(list_passed):
    list_of_index = range(0, len(list_passed)-1)

    for index in list_of_index:
        min_value = index

        for subIndex in range(index+1, len(list_passed)):

            if list_passed[subIndex] < list_passed[min_value]:
                min_value = subIndex
                print(min_value)

        if min_value != index:
            list_passed[min_value], list_passed[index] = list_passed[index], list_passed[min_value]

        return list_passed


print(selectionSort([5, 4, 9, 6, 4, 3, 7, 5, 9, 3, 10, 9, 11]))
