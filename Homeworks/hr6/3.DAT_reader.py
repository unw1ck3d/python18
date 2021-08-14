# -*- coding: cp1251 -*-
'''
�������� ���������, ������� ������� � ������� ����� ��� ����� ���� *.dat,
���������� ��������� � ������� �� ����� �� ����������.
'''

# ����������� ����������
import os # ��� ������ � �������
import pickle # ��� ������ � dat-�������

# ��� ������� ����� � ����������
for file in os.listdir():
    # �������� ��� � ���������� �����
    filename, file_extension = os.path.splitext(file)
    # ���� ��� �����, ������ ��� ������, ������������� �� .dat
    if file.endswith(".dat"):
        # ������� ����� � ������ � ����������� �����
        print(f'��������� ������� �� {filename}{file_extension}:')
        # ��������� ���� dat ����� �����
        with open(file, 'rb') as file:
            # ��������� ��� �������, ��� ������ - ��� ������� �� ������
            content = pickle.load(file)
            # ��� ������� ����� �������
            for x in content:
                # ������� ���� � �������� ����� ��� �����
                print(x, content[x])
        print('##################################################')
