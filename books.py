
import pandas as pd
import json

filename = '' #path to JSON file

class BookCollection:
    # Initialises empty object as well as loads collection.
    def __init__(self):
        self.books = {}
        self.filename = filename

        self.load_collection()

    # Initial input for user. What they wish to do with the system.
    def initial_input(self):
        while True:
            print("""
                What would you like to do with your book collection:

                >> Add
                >> Display
                >> Search
                >> Exit 
            """)
            user_input = input()
            if user_input.lower() == "exit":
                print("Farewell")
                exit()
            elif user_input.lower() == "add":
                self.add()
            elif user_input.lower() == "display":
                self.display()
            elif user_input.lower() == "search":
                self.search()
            else:
                print("Invalid input")

    # add new book
    def add(self):
        while True:
            name = input("What book do you wish to add?")
            author = input("What is the author's name?")
            new_book = {
                "name": name,
                "author": author,
            }
            self.books.append(new_book)
            self.save_collection()
            add_again = input("Would you like to add another?")
            if add_again.lower() == "no":
                break
            if add_again.lower() != "yes" and add_again.lower() != "no":
                print("Invalid input!")
                add_again = input("Would you like to add another?")

    # display collection
    def display(self):
        df = pd.DataFrame(self.books) #Display books
        print(df)

    # search collection
    def search(self):
            searched_book = input("What book do you wish to search for?")
            if searched_book in self.books.name:
                print("Book is in your collection")
            else:
                print("Book is not in your collection")

    # loads collection
    def load_collection(self):
        try:
            df = pd.read_json(self.filename)
            self.books = df["books"].tolist()
        except:
            print("File not found.")

    # saves collection
    def save_collection(self):
        try:
            data = {"books": self.books}
            with open(self.filename, "w") as file:
                json.dump(data, file, indent=4)
        except:
            print("File not found.")

book_collection = BookCollection()
book_collection.initial_input()