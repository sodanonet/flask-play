from app import app

@app.route("/")
def hello_world():
    return "<p>Hello, World 3!</p>"