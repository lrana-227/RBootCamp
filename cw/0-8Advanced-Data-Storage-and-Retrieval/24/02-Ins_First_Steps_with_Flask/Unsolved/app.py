from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    print("Server received request for 'Home' page")
    return "wELCOME TO MY 'HOME' PAGE"

@app.route("/about")
def about():
    print("Server received request for 'About' page")
    return "wELCOME TO MY 'About' PAGE"

if __name__ == "__main__":
    app.run(debug=True)

