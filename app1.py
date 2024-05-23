from utils import database
user_msg='''
App kya karna chahte hain:
    book add karne ke liye = a
    bahar jane ke liye = q
Enter your option :'''

def menu():
    user_input=input(user_msg)
    database.create_file()
    while user_input!='q':
        if user_input=='a':
            prompt_add_book()
        user_input=input(user_msg)


def prompt_add_book():
    name=input("Enter name of book")
    author=input("Enter name of author")
    database.add_book(name,author)
menu()

# def FtoT():
#     readstatus = input("Enter 'r' if you read this book")
#     if readstatus=='r':
#         name = input("Enter name of book")
#         author = input("Enter name of author")
# FtoT()
