class Libary:
    def __init__(self, list_of_books, name):
        self.booksList = list_of_books
        self.name = name
        self.lendDict = {}
    
    def displaybooks(self):
        print(f"we have the following books in our libary: {self.name}")
        for book in self.booksList:
            print(book)
    
    def lendBook(self, user, book):
        if book not in self.booksList:
            print("sorry, we do not have that book.")
        elif book in self.lendBook:
            print(f"the book is already being used by {self.lendBook[book]}")
        else:
            self.lendDict[book] = user
            print("Lender book database has been updated, you can take the book now")
        
    def addbook(self,book):
        self.booksList.append(book)
        print(f"{book} has been added to the book list")
    def returnbook(self,book):
        if book in self.lendDict[book]:
            del self.lendDict[book]
            print("book has been returned")
        else:
            print("that book wasnt borrowed from us")

if __name__ == '__main__':
    books = Libary(["Python","rich dad poor dad","harry potter","C++ basics","Algorithms by CLRS"],"Lets Upskill")
    user_name = input("Welcome to the Libary ! please enter your name: ")
    while True:
        print(f"\n hello {user_name}, welcome to the {books.name} libary please choose an option: ")
        print("1. Display books \n. 2. Lend a book, \n 3. Add a book, \n 4. Return a book, \n 5. Quit")
        user_choice = input("Enter your choice to continue:  ")
        if user_choice not in ['1','2','3','4','5']:
            print("please enter a valid option.")
            continue
        if user_choice == '1':
            books.displaybooks()
        elif user_choice == '2':
            book = input("Enter the name of the book you want to lend: ")
            books.lendBook(user_name,book)
        elif user_choice == '3':
            books = input("enter the book you want to add")
            books.addbook(book)
        elif user_choice == '4':
            book = input("enter the name of the book you want to return:  ")
            books.returnbook(book)
        elif user_choice == '5':
            print(f"thank you for using the libary, {user_name}, Goodbye!")
            break
   