# Initialize the class chatbook
class chatbook:

    __user_id = 0

    # __ini__() is one of the Special/Magic/Dunder methods - constructor
    def __init__(self):
        self.id = chatbook.__user_id
        chatbook.__user_id += 1
        self.__name = "Default User"   # Hidden atstribute
        self.username = ""
        self.password = ""
        self.loggedin = False
        # self.menu()

    @staticmethod
    def get_id():
        return chatbook.__user_id

    @staticmethod
    def set_id(val):
        chatbook.__user_id = val


    def get_name(self):
        return self.__name

    def set_name(self, value):
        self.__name = value

    def menu(self):
        user_input = input(""" \n Welcome to Chatbook \n How would like to proceed?\n
                        1. Press 1 to SignUp
                        2. Press 2 to SignIn
                        3. Press 3 to Write a Post
                        4. Press 4 to message a friend
                        5. Press any other key to exit\n  -:> """)
        
        if user_input == "1":
            self.signup()
        elif user_input == "2":
            self.signin()
        elif user_input == "3":
            self.my_post()
        elif user_input == "4":
            self.sendmsg()
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

    def my_post(self):
        if self.loggedin == True:
            txt = input("Enter your post message here -:> ")
            print(f"Following content has been posted -:> {txt}")
        else:
            print("You need to signin first to post something...")
        print("\n")
        self.menu()
    
    def sendmsg(self):
        if self.loggedin == True:
            txt = input("Enter the message:")
            frnd = input("Whom you want to send the message ? ->")
            print(f"Your message has been sent to {frnd}")
        else:
            print("You need to signin first to post something...")
        print("\n")
        self.menu()           
             
obj = chatbook()
