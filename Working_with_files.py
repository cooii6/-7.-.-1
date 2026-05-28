# ТЕМА: Робота з файлами
# Варіант 8

LINE_LENGTH = 20

file1_name = "TF11_1.txt"
file2_name = "TF11_2.txt"


def open_file(file_name, mode):
    try:
        file = open(file_name, mode, encoding="utf-8")
    except:
        print("Файл", file_name, "не вдалося відкрити!")
        return None
    else:
        print("Файл", file_name, "відкрито.")
        return file


def make_fixed_length(text, length):
    if len(text) > length:
        return text[:length]
    else:
        return text + " " * (length - len(text))


# Створення файлу TF11_1
file_1_w = open_file(file1_name, "w")

if file_1_w is not None:
    lines = [
        "Abc123def45gh67890",
        "Room7test88code999x",
        "Python2026lab15abc",
        "Data55file100text7"
    ]

    for line in lines:
        file_1_w.write(make_fixed_length(line, LINE_LENGTH) + "\n")

    file_1_w.close()
    print("Дані успішно записано у файл TF11_1.txt.")
    print("Файл TF11_1.txt закрито.")


# Обробка файлу TF11_1 і запис у TF11_2
file_1_r = open_file(file1_name, "r")
file_2_w = open_file(file2_name, "w")

if file_1_r is not None and file_2_w is not None:
    for line in file_1_r:
        digits = ""

        for symbol in line:
            if symbol.isdigit():
                digits += symbol

        result_line = make_fixed_length(digits, LINE_LENGTH)
        file_2_w.write(result_line + "\n")

    file_1_r.close()
    file_2_w.close()

    print("Файли TF11_1.txt і TF11_2.txt закрито.")


# Читання і виведення файлу TF11_2
print("\nВміст файлу TF11_2.txt:")

file_2_r = open_file(file2_name, "r")

if file_2_r is not None:
    for line in file_2_r:
        print(line.rstrip())

    file_2_r.close()
    print("Файл TF11_2.txt закрито.")