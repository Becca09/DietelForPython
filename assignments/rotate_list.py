def rotate(lists, num):  # declaring the function and giving it two parameters,
    # making num the counter and also more like the slicer

    #     newList = []  # creating a new empty list
    #
    #     for number in range((len(lists)) - num, len(lists)):
    #         newList.append(lists[number])
    #
    #     for number in range(0, len(lists) - num):
    #         newList.append(lists[number])
    #
    #     return newList
    #
    #
    # rotate_num = 2
    # list_1 = [12, 34, 56, 78, 90, 100]
    # print(rotate(list_1, rotate_num))
    if num > len(lists):
        num = num % len(lists)
    else:
        num = num
    return lists[-num:] + lists[:-num]


lst = [23, 35, 46, 59, 60]
number = 7
print(rotate(lst, number))
