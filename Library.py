#This is the student-library manegemnt sytem using Object orient programming.
class Library;
def__int__(self,listOfBooks):
self.books= listOfBooks

def displayAvailableBooks(self):
print("Books presents in this library are :")
for book in self.books:
print("*" +book)

def borrow(self,bookName):
if bookName in self.books:
print(f"You have been issued {bookName}.please keep it safe and return it within 30 days")
self.books.remove(bookName)
return True
else:
return False
