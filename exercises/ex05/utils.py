"""EX05 - 'list' Utility Functions."""

__author__ = "730406845"


def only_evens(num: list[int]) -> list[int]:
    """Returns the even integers in a list."""
    even_list: list[int] = []
    for item in num:
        if item % 2 == 0:
            even_list.append(item)
    return even_list


def sub(a_list: list[int], start_idx: int, end_idx: int) -> list[int]:
    """Generates a list which is a subset of the given list between start_idx and end_idx - 1."""
    if start_idx < 0:
        start_idx = 0 
    if end_idx > len(a_list):
        end_idx = len(a_list)
    subset_list: list[int] = []
    while start_idx < end_idx:
        subset_list.append(a_list[start_idx])
        start_idx += 1 
    return subset_list


def concat(list_1: list[int], list_2: list[int]) -> list[int]:
    """Given two lists, generate a new list which contains all of the elements of the first list followed by all of the elements of the second list."""
    new_list: list[int] = []
    idx_1: int = 0 
    idx_2: int = 0 
    while idx_1 < len(list_1):
        new_list.append(list_1[idx_1])
        idx_1 += 1 
    while idx_2 < len(list_2):
        new_list.append(list_2[idx_2])
        idx_2 += 1 
    return new_list