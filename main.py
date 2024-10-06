from new_funk import *
from defferenc import *


def main():

    print('введите первое число')
    a = int(input())
    print('введите второе число')
    b = int(input())
    print('выберите операцию. 1- сложение, 2 - разность')
    op = int(input())

    if op == 1:
        print(f'{a}+{b}={plus(a, b)}')
    elif op==2:
        print(f'{a}-{b}={differ(a, b)}')
    else:
        print(f'Такой операции нет')

if __name__ == "__main__":
    while True:
        main()