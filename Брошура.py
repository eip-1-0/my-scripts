while True:
        n = int(input('Введіть кількість сторінок: '))
        if n == 0 or n % 4 != 0:
                print('Помилка! Кількість сторінок має бути кратною чотирьом.')
        else:
                for i in range(int(n / 4)):
                        j = 2 * i
                        if i != n / 4 - 1:
                                print(n - j, j + 1, j + 2, n - j - 1, sep=', ', end=', ')
                        else:
                                print(n - j, j + 1, j + 2, n - j - 1, sep=', ')
        print()
