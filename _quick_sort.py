arr = [5, 8, 7, 9,
       0, 52, 132, 6, 8, 234, 833241, 89, 21, 68798, 2345, 7971, 234.67, 1347.742, 1235.7, 2358.1, 46, 9, 2, 346, 4.235,
       247, 25.74, 4, 3, 2, 1, 6]


def quickSort(arr, left=None, right=None):
    left = 0 if not isinstance(left, (int, float)) else left
    right = len(arr) - 1 if not isinstance(right, (int, float)) else right
    print(left, right)
    print("=")
    if left < right:
        # partitionIndex = partition(arr, left, right)
        # quickSort(arr, left, partitionIndex - 1)
        # quickSort(arr, partitionIndex + 1, right)
        partitionIndex = _partition(arr, left, right)
        quickSort(arr, left, partitionIndex - 1)
        quickSort(arr, partitionIndex + 1, right)
    return arr


def _partition(arr, left, right):
    pivot = right
    pivot_value = arr[pivot]
    right_i = right - 1
    left_i = left

    while left_i <= right_i:
        print(left_i, right_i)
        if arr[left_i] < pivot_value:
            print("AAA")
            left_i += 1
        elif left_i == right_i:
            print("BBB")
            swap(arr, left_i, pivot)
            break
        else:
            if arr[right_i] > pivot_value:
                print("CCC")
                right_i -= 1
            else:
                print("DDD")
                swap(arr, left_i, right_i)
                print(arr)
    return left_i


def partition(arr, left, right):
    pivot = left  # 轴
    index = pivot + 1  # 左指针
    i = index
    while i <= right:
        if arr[i] < arr[pivot]:  #
            swap(arr, i, index)
            index += 1
        i += 1  # 如果左指针的值 大于 轴的值, 左指针右移
    swap(arr, pivot, index - 1)
    return index - 1


def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


if __name__ == "__main__":
    result = quickSort(arr=arr)
    print(result)
