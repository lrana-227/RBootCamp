# 1. Import Flask
from flask import Flask


# 2. Create an app
app = Flask(__name__)


# 3. Define static routes
@app.route("/")
def home():
    print("Server received request for 'Home' page")
    return "Welcome to my API!"

@app.route("/about")
def about():
    print("Server received request for 'About' page")
    name = "Lipi"
    location = "Chicago"

    return f"My name is {name}, and I live in {location}."

@app.route("/contact")
def contact():
    print("Server received request for 'contact' page")
    email = "justchilax2000@yahoo.com"

    return f"Email me at {email}."

# 4. Define main behavior
if __name__ == "__main__":
    app.run(debug=True)
    