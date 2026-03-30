"""
排序工具测试 - Day 5 单元测试练习
"""
import pytest
from sort_utils import bubble_sort, quick_sort, merge_sorted_lists


class TestBubbleSort:
    """冒泡排序测试"""

    def test_normal_case(self):
        assert bubble_sort([64, 34, 25, 12, 22, 11, 90]) == [11, 12, 22, 25, 34, 64, 90]

    def test_empty_list(self):
        assert bubble_sort([]) == []

    def test_single_element(self):
        assert bubble_sort([42]) == [42]

    def test_already_sorted(self):
        assert bubble_sort([1, 2, 3]) == [1, 2, 3]

    def test_reverse_sorted(self):
        assert bubble_sort([3, 2, 1]) == [1, 2, 3]


class TestQuickSort:
    """快速排序测试"""

    def test_normal_case(self):
        assert quick_sort([64, 34, 25, 12, 22, 11, 90]) == [11, 12, 22, 25, 34, 64, 90]

    def test_empty_list(self):
        assert quick_sort([]) == []

    def test_single_element(self):
        assert quick_sort([42]) == [42]


class TestMergeSortedLists:
    """合并排序列表测试"""

    def test_normal_merge(self):
        assert merge_sorted_lists([1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6]

    def test_empty_lists(self):
        assert merge_sorted_lists([], []) == []

    def test_one_empty_list(self):
        assert merge_sorted_lists([1, 2], []) == [1, 2]
        assert merge_sorted_lists([], [1, 2]) == [1, 2]


if __name__ == "__main__":
    pytest.main([__file__, "-v"])