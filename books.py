
import pandas as pd
import json

filename = '' #path to JSON file

class BookCollection:
    # Initialises empty object as well as loads collection.
    def __init__(self):
        self.books = {}
        self.filename = filename

        self.load_collection()

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

    # Initial input for user. What they wish to do with the system.
    def initial_input(self):
        while True:
            print("""
                What would you like to do with your book collection:

                >> Add (1)
                >> Remove (2)
                >> Display (3)
                >> Search (4)
                >> Exit (q)
            """)
            user_input = input()
            if user_input.lower() == "q":
                print("Farewell")
                exit()
            elif user_input == "1":
                self.add()
            elif user_input == "2":
                self.remove()
            elif user_input == "3":
                self.display()
            elif user_input == "4":
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
            add_again = input("Would you like to add another? (y/n) ")
            if add_again.lower() == "n":
                break
            if add_again.lower() != "y" and add_again.lower() != "n":
                print("Invalid input!")
                add_again = input("Would you like to add another? (y/n) ")
    
    # remove a book
    def remove(self):
        while True:
            removed_book = input("What book do you wish to remove?")
            removed = False
            for book in self.books:
                if book['name'] == removed_book:
                    self.books.remove(book)
                    removed = True
                    break
            if removed:
                self.save_collection()
                print(f"{removed_book} has been removed from the collection.")
            else:
                print(f"{removed_book} is not found in the collection.")

            remove_again = input("Would you like to remove another? (y/n) ")
            if remove_again.lower() == "n":
                break
            if remove_again.lower() != "y" and remove_again.lower() != "n":
                print("Invalid input!")
                remove_again = input("Would you like to remove another? (y/n) ")

    # display collection
    def display(self):
        df = pd.DataFrame(self.books) #Display books
        print(df)

    # search collection
    def search(self):
            while True:
                searched_book = input("What book do you wish to search for?")
                if searched_book in self.books.name:
                    print("Book is in your collection")
                else:
                    print("Book is not in your collection")
                search_again = input("Would you like to search for another? (y/n) ")
                if search_again.lower() == 'n':
                    break

book_collection = BookCollection()
book_collection.initial_input()
