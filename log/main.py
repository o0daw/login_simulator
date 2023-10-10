import os
import time

class Main:
    def __init__(self):
        self.user = {
            'login': 'user1',
            'password': 'Qwerty',
            'pin': '1234'
        }
        self.tries = 0
    def login_window(self):
        user_login = input("Enter your login: ")
        if user_login == self.user['login']:
            pass
        else:
            self.tries += 1
            print(f"Incorrect, try to repeat ({self.tries} / 3)")
            if self.tries >= 3:
                print("You have used all tries...")
                
            self.login_window()

        user_password = input("Enter your password: ")

if __name__ == "__main__":
    app = Main()
    app.login_window()
    
