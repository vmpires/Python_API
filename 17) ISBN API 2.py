import requests

isbn_repo = open("ISBN.txt")
isbn_numbers = isbn_repo.readlines()
new_archive = open("ISBN_TITLE.txt", "a")

for isbn in isbn_numbers:
    request = requests.get(f"https://openlibrary.org/isbn/{isbn.strip()}.json")
    isbn_data = request.json()

    new_archive.write(f"ISBN nº {isbn} {isbn_data['title']}\n")
