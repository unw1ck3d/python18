# -*- coding: cp1251 -*-
'''
�������� �������� ����������� ���������� �� ������.
������������� ��� ���, ����� ���������� ������������� �� �� �����������, � �� ��������.
������������ ������ [19,2,31,45,6,11,121,27]
'''


def reverse_bubble_sort(nums):
    # ������������� �������� True ��� ����� ����������-�������������
    swapped = True
    # ���� ������������� � �������� True ���� while �������
    while swapped:
        # ����� ����� ������ ����� while ������ �������� ������������� �� False
        swapped = False
        # ��� ������� �������� ������� � ����� ��������� ��������������� ������� ����� ���� ������� �� ��������� �������
        for i in range(len(nums) - 1):
            # ���� ���������� � ����� ������� ������� ������ ��� �������� ������� � ���� �� �������
            if nums[i] < nums[i + 1]:
                # ������ �� ������� � �������
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                # ���������� ������������� � �������� True ��� ����, ����� ���� while ��������� �������
                swapped = True


nums = [19, 2, 31, 45, 6, 11, 121, 27]
reverse_bubble_sort(nums)
print(nums)