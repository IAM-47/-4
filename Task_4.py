import random
n = input('Введите количество камней: ')
try:
    n = int(n)
    if n in range(4, 31):
        while n > 1:
            hod_p = n
            hod_c = n
            while n - hod_p < 1:
                hod_p = input('Выберете какоее количество камней вы хотите убрать 1, 2 или 3: ')
                if hod_p.isdigit():
                    hod_p = int(hod_p)
                    if hod_p not in range(1, 4):
                        print('Введенные данные некорректны!')
                        break
                    if n - hod_p == 1:
                        n -= hod_p
                        print('Остался 1 камень, пользователь победил!')
                        break
                    if n - hod_p > 1:
                        n -= hod_p
                        print(f'Осталось {n} камней')
                        while n - hod_c < 1:
                            hod_c = random.randint(1, 3)
                            if n - hod_c == 1:
                                n -= hod_c
                                print('Ход компьютера: ', hod_c)
                                print('Остался один камень, компьютер победил!')
                                break
                            if n - hod_c > 1:
                                print('Ход компьютера: ', hod_c)
                                n -= hod_c
                                print(f'Осталось {n} камней')
                                break
                    if n == 1:
                        break
                else:
                    print('Введенные данные некорректны!')
                    break
    else:
        print('n должно находиться в диапазоне от 4 до 30!')
except ValueError:
    print("нужно вводить числа а не какие-то другие символы!")