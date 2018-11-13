from flask import Flask, render_template

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
    }

}

all_my_users = {
    'user1': {
        'first_name': 'John',
        'last_name': 'Smith',
        'borrowed': None,
        'given': None,
    },
    'user2': {
        'first_name': 'Thomas',
        'last_name': 'Adams',
        'borrowed': None,
        'given': None,
    }
}


app = Flask(__name__)

      # Templates
@ app.route("/")


def home():
    return render_template('index.html')


@app.route("/book/<book_id>")
def book(book_id, book_author):
    book = all_my_books[book_id]

    return render_template('book.html',
                           book_title=book['title'],
                           book_description=book['description'],
                           book_url=book['img_url'])


# Templates
@app.route("/status")
def status():
    return 'HAPPY'



@app.route("/user/<user_ID>")
def user(user_ID):
    #return user_ID

    user = all_my_users[user_ID]


    return render_template('user.html', user=user)


if __name__ == "__main__":
    app.run()
