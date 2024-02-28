def is_binary(num):
    return all(bit in '01' for bit in num)

def convert(bin_num):
    dec_num = 0
    bin_num = str(bin_num)[::-1]
    for i in range(len(bin_num)):
        if bin_num[i] == '1':
            dec_num += 2 ** i
    return dec_num

def fill_sets():
    while True:
        try:
            size = int(input("Введите количество чисел: "))
            if size > 0:
                break
            else:
                print("Количество чисел должно быть больше нуля.")
        except ValueError:
            print("Введите корректное число.")
    bin_set = set()
    dec_set = set()
    for _ in range(size):
        bin_num=input("Введите двоичное число: ")
        while not is_binary(bin_num):
            print("Это не двоичное число")
            bin_num = input("Введите двоичное число: ")
        bin_num = int(bin_num)
        if bin_num in bin_set:
            print("Вы уже добавляли данное число")
        bin_set.add(bin_num)
        dec_set.add(convert(bin_num))
    return bin_set, dec_set

def print_sets(sets):
    for bin_num, dec_num in zip(sorted(sets[0]), sorted(sets[1])):
        print(f"{bin_num} (в двоичной) = {dec_num} (в десятичной)")

def choice():
    a = fill_sets()
    while True:
        print("\n1. Заполнить новые множества")
        print("2. Вывести множество двоичных чисел")
        print("3. Вывести множество десятичных чисел")
        print("4. Вывести оба множества")
        print("5. Выход\n")
        x = input()
        if x == "1":
            a = fill_sets()
        elif x == "2":
            print(*a[0], sep=", ")
        elif x == "3":
            print(*a[1], sep=", ")
        elif x == "4":
            print_sets(a)
        elif x == "5":
            break
        else:
            print("Выберите верную команду")


choice()
