import json
import os
book_files= "database.json"

def create_file():
    if not os.path.exists(book_files):
        with open(book_files,'w') as file:
            json.dump([],file)

def add_book(name,author):
    with open(book_files,'r+') as file:
        books=json.load(file)
        books.append({'name':name,'author':author,'read':False})
        file.seek(0)
        json.dump(books,file)
        # file.truncate()