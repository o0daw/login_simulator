import os
import time
import json
from colorama import Fore, Style, init, Back

init(autoreset=True)

class Main:
    def __init__(self):
        self.users = {}
        self.tries = 0
    def load_users(self):
        if os.path.exists['users.json']:
            with open('users.json', 'r') as file:
                self.users = json.load(file)
    def save_users(self):
        with open('users.json', 'w') as file:
            json.dump(self.users, file, ident= 4)

    def login_window(self):
        user_login = input(f"{Fore.GREEN}Enter your login:{Style.RESET_ALL} ")
        if user_login == self.users:
            user_data = self.users[user_login]
            self.tries = 0
            self.pass_window(user_data)
        else:
            self.tries += 1
            print(f"{Fore.RED}Incorrect, try to repeat ({self.tries} / 3){Style.RESET_ALL}")
            if self.tries >= 3:
                print(f"{Fore.RED}You have used all tries...{Style.RESET_ALL}")
                exit()
                
            self.login_window()


    def pass_window(self,user_data):
        user_password = input(f"{Fore.GREEN}Enter your password:{Style.RESET_ALL} ")
        if user_password == self.user_data['password']:
            self.tries = 0
            if self.user_data['role'] == 'admin':
                self.admin_menu()
            else:
                self.user_menu(user_data)
            
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