from boggle import Boggle
from flask import Flask, request, render_template, redirect, flash, session, jsonify
from flask_debugtoolbar import DebugToolbarExtension


app = Flask(__name__)
app.debug = True
app.config["SECRET_KEY"] = "key"
toolbar = DebugToolbarExtension(app)

boggle_game = Boggle()

@app.route("/")
def index():
    """Homepage."""
    b_board = boggle_game.make_board()
    session["board"] = b_board
    return render_template("home.html", board = b_board)

@app.route("/check")
def check_word():
    """Checking if the word is valid."""

    word = request.args["word"]
    board = session["board"]
    response = boggle_game.check_valid_word(board, word)

    return jsonify({'result': response})

@app.route("/post-score", methods=["POST"])
def post_score():
    """Receive score, update nplays, update high score if appropriate."""

    score = request.json["score"]
    highscore = session.get("highscore", 0)
    nplays = session.get("nplays", 0)

    session['nplays'] = nplays + 1
    session['highscore'] = max(score, highscore)

    return jsonify(brokeRecord=score > highscore)
