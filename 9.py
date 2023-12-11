class Book:
    def __init__(self,title,author,genre,pub_year) -> None:
        self.title=title
        self.author=author
        self.genre=genre
        self.pub_year=pub_year
        self.display_info()
    
    def display_info(self):
        print(f"Book Title:{self.title}\nBook Author:{self.author}\nBook Genre:{self.genre}\nPublication Year:{self.pub_year}")
    
book1=Book('The Alchemist','Paulo Coelho','Philosophy','2010')