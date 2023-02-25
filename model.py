from config import *
import re


def solution():
    print("SOLUTION: ")


class Model:

    @staticmethod
    def show_mismatches():

        with open(task1_file1, "r", encoding="utf-8") as file1:
            strings1 = file1.readlines()

        with open(task1_file2, "r", encoding="utf-8") as file2:
            strings2 = file2.readlines()

        solution()

        if strings1 == strings2:
            print("Mismatches not found!")
            return

        print("Mismatched strings: ")

        if len(strings1) > len(strings2):
            for i in range(len(strings2)):
                if strings2[i] != strings1[i]:
                    print(f"First file: {strings1[i]}\nSecond file:{strings2[i]}")
        else:
            for i in range(len(strings1)):
                if strings1[i] != strings2[i]:
                    print(f"First file: {strings1[i]}Second file:{strings2[i]}")

    @staticmethod
    def show_quantities():

        vowels_quantity = 0
        consonants_quantity = 0
        numbers_quantity = 0

        with open(task2_file1, "r", encoding="utf-8") as source_file:
            strings = source_file.readlines()
            strings_quantity = len(strings)
            symbols = "".join(strings)
            symbols_quantity = len(symbols)

            for symbol in symbols:
                if symbol.isdigit():
                    numbers_quantity += 1
                if symbol in VOWELS:
                    vowels_quantity += 1
                elif symbol in CONSONANTS:
                    consonants_quantity += 1

        solution()

        with open(task2_file2, "w", encoding="utf-8") as new_file:
            new_file.write(f"Statistic about source file:\nSymbols quantity: {symbols_quantity}\n"
                           f"Strings quantity: {strings_quantity}\nVowels quantity: {vowels_quantity}\n"
                           f"Consonants quantity: {consonants_quantity}\nNumbers quantity: {numbers_quantity}")

        with open(task2_file2, "r", encoding="utf-8") as new_file:
            new_content = new_file.read()
            print(new_content)

    @staticmethod
    def delete_last_string():

        with open(task3_file1, "r", encoding="utf-8") as source_file:
            strings = source_file.readlines()

            clear_file = open(task3_file1, "w")
            clear_file.close()

        for i in range(len(strings) - 1):
            with open(task3_file1, "a", encoding="utf-8") as refactored_file:
                refactored_file.write(strings[i])

        with open(task3_file2, "w", encoding="utf-8") as new_file:
            new_file.write(strings[len(strings) - 1])

        solution()

        with open(task3_file2, "r", encoding="utf-8") as new_file:
            new_content = new_file.read()
            print(f"This string has been deleted and recorded by new file:\n{new_content}")

    @staticmethod
    def get_max_length_string():

        max_string_len = 0
        max_string = ""

        with open(task4_file, "r", encoding="utf-8") as source_file:
            strings = source_file.readlines()

        for string in strings:
            if len(string) > max_string_len:
                max_string_len = len(string)
                max_string = string

        solution()

        print(f"Max string length in the file: {max_string_len}\n"
              f"This string is: {max_string} ")

    @staticmethod
    def find_word():

        counter = 0
        search_word = (input("Enter word for search: ")).lower()

        with open(task5_file, "r", encoding="utf-8") as source_file:
            content = (re.sub(marks_punctuation, '', source_file.read())).split()

        for word in content:
            if search_word == word.lower():
                counter += 1

        solution()

        if counter > 0:
            print(f'The search word "{search_word}" was found in the file {counter} time(s).')
        else:
            print(f'Word "{search_word}" not found in the file!')

    @staticmethod
    def replace_word():

        old_word = (input("Enter word for replace: ")).lower()
        new_word = (input("Enter new word: ")).lower()

        with open(task6_file, "r", encoding="utf-8") as source_file:
            content = source_file.read()

        content = content.replace(old_word, new_word)

        with open(task6_file, "w", encoding="utf-8") as new_file:
            new_file.write(content)

        solution()
        print(f"Text after replace:\n{content}")
