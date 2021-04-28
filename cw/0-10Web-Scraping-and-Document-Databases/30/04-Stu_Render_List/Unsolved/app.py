# import necessary libraries
from flask import Flask, render_template

# create instance of Flask app
app = Flask(__name__)


# create route that renders index.html template
@app.route("/")
def index():
    movies = ["Infinity","Star Wars","Matrix","Jumanji","Akira"]
    return render_template("index.html",movie_list=movies)

if __name__ == "__main__":
    app.run(debug=True)
