from flask import Flask, render_template

app = Flask(__name__)

# Templates
@app.route("/")
def home():
    return render_template('index.html')


# Templates
@app.route("/status")
def status():
    return 'HAPPY'

if __name__ == "__main__":
    app.run()
