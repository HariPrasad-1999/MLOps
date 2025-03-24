class chatbook:
    def __init__(self):
        self.username = ""
        self.password = ""
        self.loggedin = False
        self.menu()

    def menu(self):
        user_input = input(""" Welcome to Chatbook \n How would like to proceed?\n 
                            1. Press 1 to SignUp
                            2. Press 2 to SignIn
                            3. Press 3 to Write a Post
                            4. Press 4 to message a friend
                            5. Press any other key to exit\n""")
        
        if user_input == "1":
            self.signup()
        elif user_input == "2":
            self.signin()
        elif user_input == "3":
            pass
        elif user_input == "4":
            pass
        else:
            exit()

    def signup(self):
        email = input("Enter Email -:> ")
        password = input("Enter Password -:> ")
        self.username = email
        self.password = password
        print("You have signed up successfully.")
        print("\n")
        self.menu()

    def signin(self):
        if self.username == "" and self.password=="":
            print("Please signup firstby pressing 1 in the main menu.")
        else:
            uname = input("Enter your Email/Username here -:> ")
            pwd = input("Enter your password -:>")
            if self.username == uname and self.password == pwd:
                print("You have signed up successfully !!")
                self.loggedin = True
            else:
                print("\n\n Please input correct credentials....")
        print("\n")
        self.menu()


obj = chatbook()
