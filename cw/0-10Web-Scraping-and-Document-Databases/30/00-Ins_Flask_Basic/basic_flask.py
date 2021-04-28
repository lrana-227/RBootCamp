from flask import Flask

app = Flask(__name__)

@app.route("/")
def basic_page():
    return ("My Basic Page using Flask")

if __name__=="__main__":
    app.run(debug=True)
