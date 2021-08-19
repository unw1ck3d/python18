# -*- coding: cp1251 -*-
'''
� ���������� ������ �������� ����� ������ �������� ����������.
�������� ����� ��� ������ � selection_sort. �������� ������.
'''

# ����������� ������
import random
import time


# ������� ��� ��������� ������� ��������� ����� ����� ����� n
def generated_array(n):
    # �������� ������ �� ��������� ����� n
    gen_array = [i for i in range(n)]
    # ������������ ���������� ������
    random.shuffle(gen_array)
    # ���������� ������������ ������ �� �������
    return gen_array


# ������� �� ����������
def selection_sort(input_list):
    start_time = time.time()  # ����� ������ �������
    for i in range(len(input_list)):
        min_i = i
        for j in range(i + 1, len(input_list)):
            if input_list[min_i] > input_list[j]: min_i = j
        input_list[i], input_list[min_i] = input_list[min_i], input_list[i]
    return time.time() - start_time  # ����� ���������� � ��������


def bubble_sort(nums):
    start_time = time.time()  # ����� ������ �������
    # ������������� �������� True ��� ����� ����������-�������������
    swapped = True
    # ���� ������������� � �������� True ���� while �������
    while swapped:
        # ����� ����� ������ ����� while ������ �������� ������������� �� False
        swapped = False
        # ��� ������� �������� ������� � ����� ��������� ��������������� ������� ����� ���� ������� �� ��������� �������
        for i in range(len(nums) - 1):
            # ���� ���������� � ����� ������� ������� ������ ��� �������� ������� � ���� �� �������
            if nums[i] > nums[i + 1]:
                # ������ �� ������� � �������
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                # ���������� ������������� � �������� True ��� ����, ����� ���� while ��������� �������
                swapped = True
        return time.time() - start_time


def default_sort(array):
    start_time = time.time()
    sorted(array)
    return time.time() - start_time

# - ���������� ������ ������ � ����� ����������.
# ��� ������� ��������� �� ��������� � ������� [������ ���������� ������]
print('���������� ����������:')
for scope in [1000, 2000, 5000, 10000]:
    # ������� �� ����� ���������� ��������� ��������������� � ����� ���������
    # ������� ����������� ����� �� ���������� �������, ����������� �� ���� ������ ����� �������
    print(f'���������� {scope} ���������')
    print(f'���������� ����������: {round((selection_sort(generated_array(scope))), 6)} ���.')
    print(f'����������� ����������: {round((bubble_sort(generated_array(scope))), 6)} ���.')
    print(f'����������� ����������: {round((default_sort(generated_array(scope))), 6)} ���.')
    print('')

'''
������:
���������� ���������� �������� ����� �������. ����� ������������� ��� ���������� ���������� ��������� �������.
���������� ���������� - ������������� ��������� ��� ��������� ���������� �������
����������� ���������� - �������� �������� �� �������, � ��� �� ����� ������� �� ����������.
'''