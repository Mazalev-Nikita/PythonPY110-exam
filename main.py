from conf import MODEL
import random
import json
from faker import Faker
faker_isbn = Faker()
faker_author = Faker()


def title():
    books_file = "books"
    with open(books_file, encoding="utf-8") as f:
        line = f.readlines()
        line_r = random.choice(line)
    return line_r


def year():
    year_r = random.randrange(1900, 2000, 1)
    return year_r


def pages():
    pages_r = random.randrange(10, 500, 1)
    return pages_r


def isbn13():
    isbn13_ = faker_isbn.isbn13()
    return isbn13_


def rating():
    rating = random.uniform(0, 5)
    return rating


def price():
    price = random.uniform(100, 500)
    return price


def author():
    author_ = faker_author.name()
    return author_


def gen(pk = 1):
    while True:
        yield {
            "model": MODEL,
            "pk": pk,
            "fields": {
                "title": title(),
                "year": year(),
                "pages": pages(),
                "isbn13": isbn13(),
                "rating": rating(),
                "price": price(),
                "author": author()
            }
        }
        pk = pk + 1


def main():
    books_gen = gen()
    list_ = [next(books_gen) for i in range(100)]
    with open("final.txt","w", encoding="utf-8") as f:
        json.dump(list_, f, indent= 4, ensure_ascii= False)

if __name__ == "__main__":
    main()

