"""A madlib game that compliments its users."""

from random import choice

from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful',
    'smashing', 'lovely',
]

STORIES = ['storyone', 'storytwo', 'storythree']


@app.route('/')
def start_here():
    """Display homepage."""

    return "Hi! This is the home page."


@app.route('/hello')
def say_hello():
    """Say hello to user."""

    return render_template("hello.html")


@app.route('/greet')
def greet_person():
    """Greet user with compliment."""

    player = request.args.get("person")

    compliment = choice(AWESOMENESS)

    return render_template("compliment.html",
                           person=player,
                           compliment=compliment)


@app.route('/game')
def show_madlib_form():
    """Display madlib form."""

    answer = request.args.get("start-game")

    if answer == "no":
        return render_template("goodbye.html")
    else:
        return render_template("game.html")


@app.route('/madlib')
def create_madlib():
    """Return completed madlib."""

    person = request.args.get("person")
    color = request.args.getlist("color")
    noun = request.args.get("noun")
    adjective = request.args.get("adjective")
    story = choice(STORIES)

    # user_entries = {}
    # for key in request.args:
    #     user_entries[key] = request.args.get(key)

    return render_template("madlib.html", storyone=story, person=person, colors=color,
                           noun=noun, adjective=adjective)


if __name__ == '__main__':
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True)
