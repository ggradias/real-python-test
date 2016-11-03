# ----- Flask Hello World -----------

from flask import Flask

# create the application object
app = Flask(__name__)


# error handling
app.config["DEBUG"] = True


# use decotators to link the function to a url


@app.route("/")


# define the view using a finction which return a string

#dinamic route
@app.route("/test/<search_query>")
def search(search_query):
    return "hello <strong>world</strong>"

@app.route("/")
@app.route("/hello")

def hello_world():
    return "<b>Hello</b>,World!"


@app.route("/integer/<int:value>")
def float_type(value):
    print(value+1)
    return ("correct")

@app.route("/path/<path:value>")

def path_type(value):
    print(value)
    return("correct")

@app.route("/name/<name>")

def index(name):
        if name.lower()=="michael":
            return ("Hello, {}".format(name),200)
        else:
            return("Not Found",404)

# start the development server using the run metthod

if __name__ == "__main__":
    app.run()
