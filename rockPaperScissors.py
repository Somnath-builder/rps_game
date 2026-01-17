from flask import Flask, render_template, request, session
import random

app = Flask(__name__)
app.secret_key = "rps_secret_key"  # required for session

mainDict = {"rock": 1, "paper": 0, "scissors": -1}
chDict = {1: "rock", 0: "paper", -1: "scissors"}

def game(computer, human):
    diff = computer - human
    if diff == 0:
        return "It's a Draw 🥲"
    elif diff == 1 or diff == -2:
        return "You Won 😎"
    return "You Lost 😶‍🌫"

@app.route("/", methods=["GET", "POST"])
def index():

    # Step 1: If player name not set yet
    if "player" not in session:
        if request.method == "POST" and "player" in request.form:
            session["player"] = request.form["player"]
        else:
            return render_template("index.html")

    result = ""
    comp_choice = ""
    user_choice = ""

    # Step 2: Handle game input safely
    if request.method == "POST" and "choice" in request.form:
        user_choice = request.form["choice"]
        human = mainDict[user_choice]
        computer = random.choice([1, 0, -1])

        comp_choice = chDict[computer]
        result = game(computer, human)

    return render_template(
        "index.html",
        player=session["player"],
        result=result,
        user_choice=user_choice,
        comp_choice=comp_choice
    )


if __name__ == "__main__":
    app.run(debug=True)
