# This section deals with bubble sort in Python


def bubbleSort(list_passed):
    total_len_Of_list = len(list_passed)-1
    has_swapped = True  # Now, if the swapping is true... then comes the loop
    count = 0
    forCount = 0
    while (has_swapped):
        # print("List after while loop")
        # print(list_passed)  # when the loop is true,
        # Convert the swap to false | But this comes to picture only if the swapping had been done...
        has_swapped = False
        count = count + 1
        print("While Loop Count : ", count)
        print("===================")
        for index in range(0, total_len_Of_list):
            forCount = forCount+1
            print("===================")
            print("For Loop Count : ", count)
            print("For the number", list_passed[index])
            # Enumerate the list_passed
            # If the previous element is greater than the next element
            if list_passed[index] > list_passed[index+1]:

                list_passed[index], list_passed[index +
                                                1] = list_passed[index+1], list_passed[index]  # swap the next element to the previous element

                # So the swapping happened and it got turned to true

                has_swapped = True
                print("Did Swapping happen?", has_swapped)
                print("The list now looks like", list_passed)
                print("===================")
            else:
                print("Swapping Did not happen")
                print("The list now looks like", list_passed)
                print("===================")

    return list_passed


print(bubbleSort([1, 4, 3, 7, 2]))
