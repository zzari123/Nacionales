class Book:
    def __init__(self, title, author, year_published):
        self.title = title
        self.author = author
        self.year_published = year_published

    def describe(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Year Published: {self.year_published}")


book1 = Book("Le Père Goriot ", "Honoré de Balzac", 1835)
book2 = Book("David Copperfield ", "Charles Dickens", 1849)
book3 = Book("Moby-Dick", "Herman Melville ", 1851)


book1.describe()
print() 
book2.describe()
print() 
book3.describe()