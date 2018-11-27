from flask import Flask, render_template
from  MySQLdb import connect, cursors
import os

all_my_books = {
    'book1': {
        'title': 'Little Prince',
        'description': 'This is a very nice child book',
        'img_url': 'https://cdn.waterstones.com/bookjackets/large/9781/4052/9781405288194.jpg'
    },
    'book2': {
        'title': 'Moby Dick',
        'description': 'This is book about a whale',
        'img_url': 'https://cdn.shopify.com/s/files/1/0036/2812/products/Moby_blue.jpg?v=1527114780'
    },
    'book3': {
        'title': 'Lord of the Rings',
        'description': 'The saga',
        'img_url': 'https://images-na.ssl-images-amazon.com/images/I/51EstVXM1UL._SX331_BO1,204,203,200_.jpg'
    }
    ,
    'book4': {
        'title': 'The Hobbit',
        'description': 'The little one',
        'img_url': 'hhttps://images-na.ssl-images-amazon.com/images/I/51uLvJlKpNL._SX321_BO1,204,203,200_.jpg'
    }
}


all_my_users = {
    'user1': {
        'first_name': 'John',
        'last_name': 'Smith',
        'currentBook': 'book2',
        'given': ['book3', 'book1'],
    },
    'user2': {
        'first_name': 'Thomas',
        'last_name': 'Adams',
        'currentBook': 'book1',
        'given': ['book2', 'book4'],
    }
}

app = Flask(__name__)


# Templates
@app.route("/")
def home():
    return render_template('index.html')


@app.route("/book/<book_id>")
def book(book_id):
    book = all_my_books[book_id]

    return render_template('book.html',
                           book_title=book['title'],
                           book_description=book['description'],
                           book_url=book['img_url'])


@app.route("/books")
def books():
    connection = connect(host=os.getenv('DB_HOST'), user=os.getenv('DB_USER'), passwd=os.getenv('DB_PASSWORD'),
                         db=os.getenv('DB_NAME'), cursorclass=cursors.DictCursor)
    cursor = connection.cursor()
    cursor.execute("SELECT id, title, description, imageUrl FROM books")
    books = cursor.fetchall()
    connection.close()
    return render_template('books.html', books=books)

@app.route("/users/<userId>")
def users(userId):
    connection = connect(host=os.getenv('DB_HOST'), user=os.getenv('DB_USER'), passwd=os.getenv('DB_PASSWORD'),
                         db=os.getenv('DB_NAME'), cursorclass=cursors.DictCursor)
    cursor = connection.cursor()
    cursor.execute("SELECT id, name, surname, profilePic FROM users where ID = %s;",(userId,))
    user = cursor.fetchone()
    connection.close()
    return render_template('user.html', user=user, books=books)




# Templates
@app.route("/status")
def status():
    return 'HAPPY'

if __name__ == "__main__":
    app.run()
