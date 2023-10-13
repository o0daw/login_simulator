class Main:

    def __init__(self):

        self.a = {
            'user' : 'qwerty',
            'pass' : '12345'
        }
    def user_window(self):
        user_input = input("Choose function user or pass: ")
        if user_input == 'user':
            print(self.a['user'])
            user_input = input("Enter new user name: ")
            self.a['user'] = user_input
            print(self.a['user'])

        if user_input == 'pass':
            print(self.a['pass'])
            user_input = input("Enter new password: ")
            self.a['pass'] = user_input
            print(self.a['pass'])
        self.user_window()
Main().user_window()
        
