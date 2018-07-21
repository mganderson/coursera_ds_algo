import copy
import random


def get_random_pivot(lst, begin, end):
    return random.randrange(begin, end)


def quicksort(lst, choose_pivot=get_random_pivot):
    """Wrapper around quicksort_recur

    lst: The list to be sorted in place
    choose_pivot: The function used to choose the pivot element.  Takes
        three arguments corresponding to lst, first index in lst
        (i.e., 0 initally), and len(list), respectively
    """
    return quicksort_recur(lst, 0, len(lst), choose_pivot)


def quicksort_recur(lst, begin, end, choose_pivot):
    """Sort a list in place

    lst: The entire list (rather than list segment this occurance
        of quicksort is to sort).  For the first occurance of
        quicksort_recur, len(lst) == end (that is, the entire list
        is the list to be sorted)
    begin: The first index of the list segment to be sorted
    end: The index beyond the last element of the list segment
        to be sorted
    choose_pivot: The function used to choose the pivot element.  Takes
        three arguments: lst, begin, end
    """
    comparisons = 0

    if end - begin <= 1:
        return comparisons

    pivot_idx = choose_pivot(lst, begin, end)
    pivot_val = lst[pivot_idx]

    # Move pivot element to front of lst segment
    lst[begin], lst[pivot_idx] = lst[pivot_idx], lst[begin]

    # Partition lst segment in terms of size relative to pivot_val
    j = begin + 1
    for i in range(begin + 1, end):
        if lst[i] < pivot_val:
            lst[i], lst[j] = lst[j], lst[i]
            j += 1
        i += 1
    # Move pivot element between elements larger than / smaller than it
    lst[begin], lst[j-1] = lst[j-1], lst[begin]

    # Recursively call quicksort on the partitioned sections
    comparisons += quicksort_recur(lst, begin, j-1, choose_pivot)
    comparisons += len(lst[begin:j-1])
    comparisons += quicksort_recur(lst, j, end, choose_pivot)
    comparisons += len(lst[j:end])
    return comparisons


def median_of_three_old(lst, begin, end):
    """Strategy for selecting pivot index OLD

    The index of the median element among the first, last,
    and middle elements in the lst segment is returned
    """
    print("Input array: {}".format(lst[begin: end]))
    print("Full array: {}".format(lst))
    first = lst[begin]
    final = lst[end - 1]
    print("middle = lst((end - begin) // 2) + begin]: {} = lst[{}]".format(lst[((end - begin) // 2) + begin - 1], ((end - begin) // 2) + begin - 1))
    middle = lst[((end - begin) // 2) + begin - 1]
    print([first, final, middle])
    print(sorted([first, final, middle]))
    if first <= middle <= final or final <= middle <= first:
        return ((end - begin) - 1) // 2
    elif middle <= first <= final or final <= first <= middle:
        return begin
    else:
        return end - 1


def median_of_three(lst, left, right):
    """Requires that all elements in lst be distinct"""
    d = {
        lst[left]: left,
        lst[(((right - left) - 1) // 2) + left]: (((right - left) - 1) // 2) + left,
        lst[right - 1]: right - 1
    }
    # print(d)
    three = [key for key in d]
    three.sort()
    # print(three)
    # print("Input array: {} left: {} right: {} middle: {} median: {}".format(lst[left:right], lst[left], lst[right - 1], lst[(((right - left) - 1) // 2) + left], three[1]))
    return d[three[1]]


def main():
    with open("input.txt", "r", encoding="UTF-8") as file:
        lst = [int(line) for line in file.readlines()]

    # Use first element in lst segment as pivot
    print(quicksort(copy.deepcopy(lst),
                    choose_pivot=lambda lst, begin, end: begin))

    # Use last element in lst segment as pivot
    print(quicksort(copy.deepcopy(lst),
                    choose_pivot=lambda lst, begin, end: end - 1))

    # Use median of first, last, and middle elements as pivot
    print(quicksort(copy.deepcopy(lst),
                    choose_pivot=median_of_three))

    # Use random pivot
    print(quicksort(copy.deepcopy(lst)))


if __name__ == "__main__":
    main()
