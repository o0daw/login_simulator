import os
import time
from colorama import Fore, Style, init, Back

init(autoreset=True)

class Main:
    def __init__(self):
        self.user = {
            'login': 'user1',
            'password': 'Qwerty',
            'pin': '1234'
        }
        self.admin = {
            'login': 'admin',
            'password': 'Qwerty',
            'pin': '1234'
        }
        self.tries = 0
    def login_window(self):
        user_login = input(f"{Fore.GREEN}Enter your login:{Style.RESET_ALL} ")
        if user_login == self.user['login'] or user_login == self.admin['login']:
            self.tries = 0
            self.pass_window()
        else:
            self.tries += 1
            print(f"{Fore.RED}Incorrect, try to repeat ({self.tries} / 3){Style.RESET_ALL}")
            if self.tries >= 3:
                print(f"{Fore.RED}You have used all tries...{Style.RESET_ALL}")
                exit()
                
            self.login_window()


    def pass_window(self):
        user_password = input(f"{Fore.GREEN}Enter your password:{Style.RESET_ALL} ")
        if user_password == self.user['password'] or user_password == self.admin['password']:
            self.tries = 0
            if str(self.user['pin']) == str("") or str(self.admin['pin']) == str(""):
                pass
            else:
                self.pin_window()
            
        else:
            self.tries += 1
            print(f"{Fore.RED}Incorrect, try to repeat ({self.tries} / 3){Style.RESET_ALL}")
            if self.tries >= 3:
                print(f"{Fore.RED}You have used all tries...{Style.RESET_ALL}")
                exit()
                
            self.pass_window()

    def pin_window(self):
        user_pin = input(f"{Fore.GREEN}Enter your pin:{Style.RESET_ALL} ")
        if user_pin == self.user['pin'] or user_pin == self.admin['pin']:
            pass
        else:
            self.tries += 1
            print(f"{Fore.RED}Incorrect, try to repeat ({self.tries} / 3){Style.RESET_ALL}")
            if self.tries >= 3:
                print(f"{Fore.RED}You have used all tries...{Style.RESET_ALL}")
                exit()
                
            self.pass_window()

    def user_menu(self):
        print("""

""")

if __name__ == "__main__":
    app = Main()
    app.login_window()
    app.pass_window()
    app.pin_window()
    app.user_menu()

# перенести словник в тхт 
# додати меню користувача(встановити нік, зміна паролю, зміна пін, відправка смс)
# додати меню адміна(вивести весь список користувачів, зміна логіна, зміна паролю, зміна пін, змінити нік, видалити користувача)