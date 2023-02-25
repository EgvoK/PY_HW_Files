import os
import sys

import view
from view import *
from model import Model


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


class Controller:
    OPTIONS = {
        '1': 'Display task 1 and execute its solution',
        '2': 'Display task 2 and execute its solution',
        '3': 'Display task 3 and execute its solution',
        '4': 'Display task 4 and execute its solution',
        '5': 'Display task 5 and execute its solution',
        '6': 'Display task 6 and execute its solution',
        '0': 'Exit'
    }

    def __init__(self):
        self.model = Model()

    def menu(self):
        cls()
        self.show_menu()

        while True:
            option = input("\nEnter the option number: ")
            cls()
            self.show_menu()
            if option in self.OPTIONS.keys():
                if option == "1":
                    view.DisplayTask1.display()
                    self.model.show_mismatches()

                if option == "2":
                    view.DisplayTask2.display()
                    self.model.show_quantities()

                if option == "3":
                    view.DisplayTask3.display()
                    self.model.delete_last_string()

                if option == "4":
                    view.DisplayTask4.display()
                    self.model.get_max_length_string()

                if option == "5":
                    view.DisplayTask5.display()
                    self.model.find_word()

                if option == "6":
                    view.DisplayTask6.display()
                    self.model.replace_word()

                if option == "0":
                    print("Exit...")
                    sys.exit()

            else:
                print("Error! Incorrect option number!")

    def show_menu(self):
        MenuDisplay.display(self.OPTIONS)

