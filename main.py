def save_history(string_s,string_h):
    f = open("history.txt", 'a')
    f.write(f"{string_s} {string_h} \n")
    f.close()

def read_history():
    try:
        f = open("history.txt", 'r')
        for line in f:
            print(line)
        f.close()
    except FileNotFoundError:
        print("Истории не существует.")

def input_symbols():
    while True:
        string = str(input("Введите символы: "))
        return string

def dots_count(string):
    count_i = 0
    for i in string:
        if i == ".":
            count_i += 1
            if count_i == 3:
                break
        else:
            count_i = 0
    if count_i == 3:
        print("Три стоящие рядом точки встречаются. \n")
        save_history(string, "Три стоящие рядом точки встречаются.")
    else:
        print("Три стоящие рядом точки не встречаются. \n")
        save_history(string, "Три стоящие рядом точки не встречаются.")


def main():
    while True:
        print("Для просмотра истории введите 0: ")
        print("Для проверки символов введите 1: ")
        print("Для завершения программы введите 2: ")
        input_inf = int(input("Введите цифру: "))
        if input_inf == 1:
            strings = input_symbols()
            dots_count(strings)
            continue
        elif input_inf == 0:
            read_history()
        else:
            exit(0)

if __name__ == "__main__":
    main()


