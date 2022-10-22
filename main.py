# -*- coding: cp1251 -*-
from random import randint


def attack(char_name: str, char_class: str) -> str:
    if char_class == 'warrior':
        return (f'{char_name} ���� ���������� ����,'
                f' ������ {5 + randint(3, 5)}')
    if char_class == 'mage':
        return (f'{char_name} ���� ���������� ����,'
                f' ������ {5 + randint(5, 10)}')
    if char_class == 'healer':
        return (f'{char_name} ���� ���������� ����,'
                f' ������ {5 + randint(-3, -1)}')
    return (f'{char_name} ���� ���������� ����,'
            f' ������ {5}')


def defence(char_name: str, char_class: str) -> str:
    if char_class == 'warrior':
        return (f'{char_name} ����������'
                f'{10 + randint(5, 10)} �����')
    if char_class == 'mage':
        return (f'{char_name} ����������'
                f'{10 + randint(-2, 2)} �����')
    if char_class == 'healer':
        return (f'{char_name} ����������'
                f'{10 + randint(2, 5)} �����')
    return (f'{char_name} ����������'
            f'{10} �����')


def special(char_name: str, char_class: str) -> str:
    if char_class == 'warrior':
        return (f'{char_name} ��������'
                f'����������� ������ '
                f'������������� {80 + 25}�')
    if char_class == 'mage':
        return (f'{char_name} ��������'
                f'����������� ������ ������ {5 + 40}�')
    if char_class == 'healer':
        return (f'{char_name} ��������'
                f'����������� ������ '
                f'������� {10 + 30}�')
    return (f'{char_name} �� �������� '
            f'����������� ������')


def start_training(char_name: str, char_class: str) -> str:
    if char_class == 'warrior':
        print(f'{char_name}, �� ������� � '
              f'������� ������ �������� ���.')
    if char_class == 'mage':
        print(f'{char_name}, �� ��� � '
              f'������������ ���������� ������.')
    if char_class == 'healer':
        print(f'{char_name}, �� ������ � '
              f'�������, ��������� �������� ����.')
    print('������������ ��������� '
          '������ ��������.')
    print('����� ���� �� ������: attack � '
          '����� ��������� ����������, '
          'defence � ����� ����������� '
          '����� ���������� ��� '
          'special � ����� ������������ '
          '���� ���������.')
    print('���� �� ������ �������������, '
          '����� ������� skip.')
    cmd: str = ''
    while cmd != 'skip':
        cmd = input('����� �������: ')
        if cmd == 'attack':
            print(attack(char_name, char_class))
        if cmd == 'defence':
            print(defence(char_name, char_class))
        if cmd == 'special':
            print(special(char_name, char_class))
    return '���������� ��������.'


def choice_char_class() -> str:
    approve_choice: str = ''
    char_class: str = ''
    while approve_choice != 'y':
        char_class = input('����� �������� ���������, '
                           '�� �������� ������ ������: '
                           '������� � warrior, '
                           '��� � mage, ������ � healer: ')
        if char_class == 'warrior':
            print('������� � ������� ���� '
                  '�������� ���. '
                  '�������, ���������� � ��������.')
        if char_class == 'mage':
            print('��� � ���������� ���� '
                  '�������� ���. '
                  '�������� ������� �����������.')
        if char_class == 'healer':
            print('������ � �������������� '
                  '�����������. '
                  '������� ���� �� �������, '
                  '���� � �����.')
        approve_choice = input('����� (Y), ����� '
                               '����������� �����, '
                               '��� ����� ������ ������, '
                               '����� ������� ������� '
                               '��������� ').lower()
    return char_class


if __name__ == '__main__':
    run_screensaver()
    print('����������� ����, �������� �����������!')
    print('������ ��� ������ ����...')
    char_name: str = input('...������ ����: ')
    print(f'����������, {char_name}! '
          '������ ���� ������������ � 80, ����� � 5 � ������ � 10.')
    print('�� ������ ������� ���� �� ��� ����� ����:')
    print('�������, ���, ������')
    char_class: str = choice_char_class()
    print(start_training(char_name, char_class))