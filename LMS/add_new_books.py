import pandas as pd

book_name = input("Please enter the name of the book to be added: ")
author_name = input("Please enter the Author's name of the book: ")
publisher_name = input("Please enter the Pulisher's name of the book: ")

#df = pd.read_csv('LMS/resources/library.csv')
data = {f'book_id': [2],
        'book_name': [book_name],
        'author_name': [author_name],
         'publisher_name': [publisher_name] }
df = pd.DataFrame(data)
df.to_csv('LMS/resources/library.csv', mode = 'a', header = False, index=False)