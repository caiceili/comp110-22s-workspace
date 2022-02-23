"""Tests for the 'list' Utility Functions."""

__author__ = "730406845"

from utils import only_evens, sub, concat


def test_only_evens_empty() -> None: 
    num: list[int] = []
    assert only_evens(num) == []


def test_only_evens_many_items() -> None: 
    num: list[int] = [10, 13, 15, 20, 28]
    assert only_evens(num) == [10, 20, 28]


def test_only_evens_only_odds() -> None: 
    num: list[int] = [27, 33, 19, 3]
    assert only_evens(num) == []


def test_sub_many_items() -> None: 
    a_list: list[int] = [10, 20, 30, 40, 50, 60] 
    assert sub(a_list, 2, 4) == [30, 40]


def test_sub_many_items_a_second_time() -> None:
    a_list: list[int] = [3, 6, 80, 34, 5, 2, 7, 10]
    assert sub(a_list, 0, 7) == [3, 6, 80, 34, 5, 2, 7]


def test_sub_start_idx_less_than_zero() -> None: 
    a_list: list[int] = [-2, -3, 1, 4, 5]
    assert sub(a_list, -1, 3) == [-2, -3, 1]


def test_sub_end_idx_greater_than_len_of_list() -> None:
    a_list: list[int] = [70, 3, 17, 6, 5]
    assert sub(a_list, 1, 7) == [3, 17, 6, 5]


def test_concat_both_empty() -> None: 
    list_1: list[int] = []
    list_2: list[int] = []
    assert concat(list_1, list_2) == []


def test_concat_list_1_empty() -> None: 
    list_1: list[int] = []
    list_2: list[int] = [3, 7, 10, 5, 6]
    assert concat(list_1, list_2) == [3, 7, 10, 5, 6]


def test_concat_list_2_empty() -> None: 
    list_1: list[int] = [5, 7, 89, 3, 6, 16]
    list_2: list[int] = []
    assert concat(list_1, list_2) == [5, 7, 89, 3, 6, 16]


def test_concat_many_items() -> None: 
    list_1: list[int] = [5, 7, 89, 3, 6, 16]
    list_2: list[int] = [10, 12, 71, 33, 45]
    assert concat(list_1, list_2) == [5, 7, 89, 3, 6, 16, 10, 12, 71, 33, 45]