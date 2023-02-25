class MenuDisplay:
    @staticmethod
    def display(option):
        print("-" * 100)
        print("Homework - Files\nThe following commands are available: ")
        for key, value in option.items():
            print(f"{key}. {value}")
        print("\n")


class DisplayTask1:
    @staticmethod
    def display():
        print("TASK 1:\nДано два текстовых файла.\nВыяснить, совпадают ли их строки.\n"
              "Если нет, то вывести несовпадающую строку из каждого файла.\n")


class DisplayTask2:
    @staticmethod
    def display():
        print("TASK 2:\nДан текстовый файл.\n"
              "Необходимо создать новый файл и записать в него следующую статистику по исходному файлу:\n"
              "- Количество символов;\n- Количество строк;\n- Количество гласных букв;\n -Количество согласных букв;\n"
              "- Количество цифр.\n")


class DisplayTask3:
    @staticmethod
    def display():
        print("TASK 3:\nДан текстовый файл.\nУдалить из него последнюю строку.\nРезультат записать в другой файл.\n")


class DisplayTask4:
    @staticmethod
    def display():
        print("TASK 4:\nДан текстовый файл.\nНайти длину самой длинной строки.\n")


class DisplayTask5:
    @staticmethod
    def display():
        print("TASK 5:\nДан текстовый файл.\nПосчитать сколько раз в нем встречается заданное пользователем слово.\n")


class DisplayTask6:
    @staticmethod
    def display():
        print("TASK 6:\nДан текстовый файл.\nНайти и заменить в нем заданное слово.\n"
              "Что искать и на что заменять определяется пользователем.\n")
