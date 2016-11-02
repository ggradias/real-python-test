# ----- Flask Hello World -----------


from flask import Flask

# create the application object
app = Flask(__name__)

# use decotators to link the function to a url


@app.route("/")
@app.route("/hello")

# define the view using a finction which return a string

def hello_world():
    return "Hello,World!"

# start the development server using the run metthod

if __name__ == "__main__":
    app.run()


