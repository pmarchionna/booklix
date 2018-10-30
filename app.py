from flask import Flask


app = Flask(__name__)

# Templates
@app.route("/")
def home():
    return 'HELLO man, how you doing, are you going to find darwins shit?'


# Templates
@app.route("/status")
def status():
    return 'HAPPY'

if __name__ == "__main__":
    app.run()
