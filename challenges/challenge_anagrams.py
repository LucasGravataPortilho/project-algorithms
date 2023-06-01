def quick_sort(string, start, end):
    if start < end:
        p = partition(string, start, end)
        quick_sort(string, start, p - 1)
        quick_sort(string, p + 1, end)


def partition(string, start, end):
    pivot = string[end]
    delimiter = start - 1

    for index in range(start, end):
        if string[index] <= pivot:
            delimiter = delimiter + 1
            string[index], string[delimiter] = string[delimiter], string[index]

    string[delimiter + 1], string[end] = string[end], string[delimiter + 1]

    return delimiter + 1


def is_anagram(first_string: str, second_string: str):
    if len(first_string) < 1 and len(second_string) < 1:
        return (first_string, second_string, False)

    lower_first_string = list(first_string.lower())
    lower_second_string = list(second_string.lower())

    quick_sort(lower_first_string, 0, len(lower_first_string) - 1)
    quick_sort(lower_second_string, 0, len(lower_second_string) - 1)

    sorted_first = ''.join(lower_first_string)
    sorted_second = ''.join(lower_second_string)
    # print(sorted_first, sorted_second)

    if sorted_first != sorted_second:
        return (sorted_first, sorted_second, False)

    if len(sorted_first) != len(sorted_second):
        return (sorted_first, sorted_second, False)

    return (sorted_first, sorted_second, True)
