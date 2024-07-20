numbers = [1, 3, 4, 5, 7, 8, 9, 13, 18, 19, 20, 24, 26, 27, 30, 33, 35, 40]


def binary_search(val, a_list):
    n = len(a_list)
    result_ok = False
    first = 0
    last = n - 1
    pos = -1
    while first < last:
        middle = (first + last) // 2
        if val == a_list[middle]:
            first = middle
            last = first
            result_ok = True
            pos = middle
        else:
            if val > a_list[middle]:
                first = middle + 1
            else:
                last = middle - 1
    if result_ok:
        print("Элемент найден")
        print(pos)
    else:
        print("Элемент не найден")


binary_search(35, numbers)


unsorted_numbers = [312, 100, 78, 99, 36, 500, 444, 123]


def bubble_sort(unsorted_list):
    length = len(unsorted_list)
    changed = True
    while changed:
        changed = False
        for i in range(length - 1):
            if unsorted_list[i] > unsorted_list[i + 1]:
                unsorted_list[i], unsorted_list[i + 1] = unsorted_list[i + 1], unsorted_list[i]
                changed = True
    print(unsorted_list)


bubble_sort(unsorted_numbers)
