# Insertion Sort :  Revision

def insertionSort(list_passed):
    list_of_index = range(1, len(list_passed))
    for index in list_of_index:
        value_to_sort = list_passed[index]

        while list_passed[index-1] > value_to_sort and index > 0:
            list_passed[index], list_passed[index -
                                            1] = list_passed[index-1], list_passed[index]
            index = index - 1

    return list_passed


print(insertionSort([5, 4, 9, 6, 4, 3, 7, 5, 9, 3, 10, 9, 11]))
