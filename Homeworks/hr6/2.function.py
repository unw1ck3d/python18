# -*- coding: cp1251 -*-
"""
�������� �������, �������:
- ��������� �� ���� �������� �����;
- ������������ � ������� �� ����� �������� �����, ����� �������� � ������� ������;
- ������� �������, ���������� ������ ������ ��������� �����;
- ��������� ������� � pickle-������� � ���� � ������ ���_�����.dat
�������� ������� � ����� ��� ���� ���������� ������.
����������� set ��� ��������� ����������� ������ ������.
"""

shows = {'��������� ���������': {'����': '����������', '�������': 0.9},
         '�������': {'����': '�������', '�������': 0.95},
         '���� �������': {'����': '��������', '�������': '0.8'},
         '24': {'Genre': '�����', 'Rating': 0.75},
         '������ �������': {'����': '����������', '�������': 0.98},
         '�� ��� ������': {'����': '��������', '�������': '0.85'},
         '���� ���������': {'����': '�������', '�������': 0.87},
         '��������� �����': {'Genre': '�����', 'Rating': 0.82},
         '��� � �����': {'����': '����������', '�������': 1}}

# ������ ���������
from functools import reduce
import pickle

# �������� ���������, �.�. �� ����������� �������� ������
genres = set()
for x in shows.values():
    try:
        genres.add(x['����'])
    except KeyError:
        genres.add(x['Genre'])

# print(genres)

# ������� �������, ������� ��������� �� ���� �������� �����
def create_dat(genre):
    rating = []  # ������� ������ ������
    genre_shows_dict = dict()  # ������� ������ �������
    file_name = genre + '.dat'  # ���������� ������� ��� � ���������� �����

    # ��� ������� �������� � ������
    for x in shows.keys():
        # �������
        try:
            # ���� �������� ����� ��� ������������� ����������� � ������� ������������
            if shows[x]['Genre'] == genre:
                # ��������� � ������ ������� ����� � ���� ���� ������ �����
                rating.append(float(shows[x]['Rating']))
                # ������� �������, ��������� ���� � �������
                genre_shows_dict.update({x: shows[x]['Rating']})
        # ���� �������� ���������� ������-�����, �.�. ����� � ����������� ������� � �������� � � ���������
        except KeyError:
            # ���� �������� ����� ��� ������������� ����������� � ������� ������������
            if shows[x]['����'] == genre:
                # ��������� � ������ ������� ����� � ���� ���� ������ �����
                rating.append(float(shows[x]['�������']))
                # ������� �������, ��������� ���� � �������
                genre_shows_dict.update({x: shows[x]['�������']})

    # �������� ������� ������� �� �������� ����� ��� ����������� � �������
    average_rating = round(reduce(lambda x, y: x + y, rating) / len(rating), 2)

    # ��������� ����, ��� ����� ��� ������
    file = open(file_name, 'wb')
    # ������ ���� ������ ������� � ����
    pickle.dump(genre_shows_dict, file)
    # ��������� ����
    file.close()

    # ���������� �� ����� �������� �����, ���������� �������� � ������� ������
    return f' {genre.title()} - {len(rating)} �������. ������� ������� {average_rating}'


# �������� ������� � ����� ��� ���� ���������� ������.
for item in genres:
    print(create_dat(item))