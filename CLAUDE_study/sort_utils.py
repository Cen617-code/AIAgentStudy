"""
排序工具模块 - Day 5 代码编写练习
"""


def bubble_sort(arr: list[int]) -> list[int]:
    """
    冒泡排序算法

    Args:
        arr: 待排序的整数列表

    Returns:
        排序后的新列表

    Example:
        >>> bubble_sort([64, 34, 25, 12, 22, 11, 90])
        [11, 12, 22, 25, 34, 64, 90]
    """
    result = arr.copy()
    n = len(result)
    for i in range(n):
        for j in range(0, n - i - 1):
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]
    return result


def quick_sort(arr: list[int]) -> list[int]:
    """
    快速排序算法

    Args:
        arr: 待排序的整数列表

    Returns:
        排序后的新列表

    Example:
        >>> quick_sort([64, 34, 25, 12, 22, 11, 90])
        [11, 12, 22, 25, 34, 64, 90]
    """
    if len(arr) <= 1:
        return arr.copy()

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)


def merge_sorted_lists(list1: list[int], list2: list[int]) -> list[int]:
    """
    合并两个已排序的列表

    Args:
        list1: 第一个已排序列表
        list2: 第二个已排序列表

    Returns:
        合并后的新列表（已排序）

    Example:
        >>> merge_sorted_lists([1, 3, 5], [2, 4, 6])
        [1, 2, 3, 4, 5, 6]
    """
    return sorted(list1 + list2)


if __name__ == "__main__":
    # 测试代码
    test_data = [64, 34, 25, 12, 22, 11, 90]

    print("原始数据:", test_data)
    print("冒泡排序:", bubble_sort(test_data))
    print("快速排序:", quick_sort(test_data))

    list_a = [1, 3, 5, 7]
    list_b = [2, 4, 6, 8]
    print(f"合并 {list_a} 和 {list_b}:", merge_sorted_lists(list_a, list_b))