from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session, url_for
from flask_session import Session
from passlib.apps import custom_app_context as pwd_context
from tempfile import mkdtemp

from helpers import *

# configure application
app = Flask(__name__)

# ensure responses aren't cached
if app.config["DEBUG"]:
    @app.after_request
    def after_request(response):
        response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
        response.headers["Expires"] = 0
        response.headers["Pragma"] = "no-cache"
        return response

# custom filter
app.jinja_env.filters["usd"] = usd

# configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")
@app.route("/")
@login_required
def index():

    index_symbols= db.execute("SELECT Shares, Symbol FROM portfolio WHERE id = :id", id=session["user_id"])

    total_cash=0

    for indexes in index_symbols:

        symbol = indexes["Symbol"]
        shares = indexes["Shares"]
        stock = lookup(symbol)
        total_added = shares * stock["price"]
        total_cash += total_added

        db.execute("UPDATE portfolio SET Price=:price, \
                    Total=:total WHERE id=:id AND Symbol=:symbol", \
                    price=usd(stock["price"]), \
                    total=usd(total_added), id=session["user_id"], symbol=symbol)


    new_cash= db.execute("SELECT cash FROM users \
                               WHERE id=:id", id=session["user_id"])

    total_cash += new_cash[0]["cash"]

    # print portfolio in index homepage
    new_portfolio = db.execute("SELECT * from portfolio \
                                    WHERE id=:id", id=session["user_id"])


    return render_template("index.html", stocks=new_portfolio, \
                            cash=usd(new_cash[0]["cash"]), total= usd(total_cash) )


    return apology("Error")

@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock."""

    if request.method=="POST":

        buy_stock=lookup(request.form.get("search"))

        #Did they enter symbol
        if not request.form.get("search"):
            return apology("Please enter a symbol")

        #Did they enter share
        elif not request.form.get("shares"):
            return apology("Please enter the number of shares you wish to buy")

        #Did they enter valid symbol
        elif not buy_stock:
            return apology("Please enter a valid symbol")

        if not request.form.get("shares").isnumeric():
            return apology("Please enter an integer value")

        #Did they enter positive number of shares
        if int(request.form.get("shares"))<=0:
            return apology("Please enter a positive number of shares")


        #get user cash
        user_cash= db.execute("SELECT cash FROM users WHERE id = :id", \
                            id=session["user_id"])
        shares= int(request.form.get("shares"))

        #Find their money
        if not user_cash:
            return apology("Error obtaining money from your account")

        #Do they have enough money for purchase
        if float(user_cash[0]["cash"]) < buy_stock["price"] * shares:
            return apology("You have insufficient funds for this purchase")

        #Update cash
        else:
            db.execute("UPDATE users SET cash = cash - :transaction WHERE id = :id", id=session["user_id"], \
                    transaction=float(shares*buy_stock["price"]))

        #UPDATE HISTORY
        db.execute("INSERT INTO transactions (symbol, shares, price, id) \
                        VALUES(:symbol, :shares, :price, :id)", \
                        shares=shares, price=usd(buy_stock["price"]), \
                        symbol=buy_stock["symbol"], id=session["user_id"])


        new_transaction= db.execute("SELECT Shares FROM portfolio \
                           WHERE id=:id AND symbol=:symbol", \
                           id=session["user_id"], symbol=buy_stock["symbol"])

        if not new_transaction:
            db.execute("INSERT INTO portfolio (Symbol, Name, Shares, Price, Total, id) \
                        VALUES(:symbol, :name, :shares, :price, :total, :id)", \
                        name=buy_stock["name"], shares=shares, price=usd(buy_stock["price"]), \
                        total=usd(shares * buy_stock["price"]), \
                        symbol=buy_stock["symbol"], id=session["user_id"])
        else:
            new_shares=new_transaction[0]["Shares"]+shares
            db.execute("UPDATE portfolio SET Shares=:shares \
                        WHERE id=:id AND Symbol=:symbol", \
                        id=session["user_id"], shares=new_shares, symbol=buy_stock["symbol"])

        return redirect(url_for("index"))

    else:
        return render_template("buy.html")

    return apology("Error")

@app.route("/history")
@login_required
def history():
    """Show history of transactions."""
    transaction_history= db.execute("SELECT * FROM transactions WHERE id = :id", \
                            id=session["user_id"])
    return render_template("history.html", transaction_history=transaction_history)
    return apology("Error")

@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in."""

    # forget any user_id
    session.clear()

    # if user reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username")

        # ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password")

        # query database for username
        rows = db.execute("SELECT * FROM users WHERE username = :username", username=request.form.get("username"))

        # ensure username exists and password is correct
        if len(rows) != 1 or not pwd_context.verify(request.form.get("password"), rows[0]["hash"]):
            return apology("invalid username and/or password")

        # remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # redirect user to home page
        return redirect(url_for("index"))

    # else if user reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")

@app.route("/logout")
def logout():
    """Log user out."""

    # forget any user_id
    session.clear()

    # redirect user to login form
    return redirect(url_for("login"))

@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""

    if request.method=="POST":

        quote123=lookup("symbol")
        quote_stock=lookup(request.form.get("search"))

        if not request.form.get("search"):
            return apology("Please enter a symbol")

        elif not quote_stock:
            return apology("Please enter a valid symbol")

        return render_template("quoted.html", quote123=quote_stock)

    else:
        return render_template("quote.html")

    return apology("Error")

@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method=="POST":

        if not request.form.get("username"):
            return apology("Please provide a username.")

        elif not request.form.get("password"):
            return apology("Please provide a password.")

        elif request.form.get("password") != request.form.get("check_password"):
            return apology("Your confirmation password does not match your original.")

        result = db.execute("INSERT INTO users (username, hash) \
                             VALUES(:username, :hash)", username=request.form.get("username"), hash=pwd_context.hash(request.form.get("password")))


        if not result:
            return apology("Username already exists")


        session["user_id"] = result

        return redirect(url_for("index"))
    else:
        return render_template("register.html")

@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock."""
    if request.method=="POST":

        sell_stock=lookup(request.form.get("search"))

        #Did they enter symbol
        if not request.form.get("search"):
            return apology("Please enter a symbol")

        #Did they enter share
        elif not request.form.get("shares"):
            return apology("Please enter the number of shares you wish to buy")

        #Did they enter valid symbol
        elif not sell_stock:
            return apology("Please enter a valid symbol")

        if not request.form.get("shares").isnumeric():
            return apology("Please enter an integer value")

        #Did they enter positive number of shares
        if int(request.form.get("shares"))<=0:
            return apology("Please enter a positive number of shares")

        #get user shares
        user_shares= db.execute("SELECT Shares FROM portfolio WHERE id = :id AND Symbol=:symbol", \
                            id=session["user_id"], symbol=request.form.get("search").upper())
        shares= int(request.form.get("shares"))

        #Find their shares
        if not user_shares:
            return apology("You do not have shares of this stock")

        #Do they have enough shares to sell
        if float(user_shares[0]["Shares"]) < shares:
            return apology("You don't have enough shares.")

        #Update cash
        else:
            db.execute("UPDATE users SET cash = cash + :transaction WHERE id = :id", id=session["user_id"], \
                    transaction=float(shares*sell_stock["price"]))

        #UPDATE HISTORY
        db.execute("INSERT INTO transactions (symbol, shares, price, id) \
                        VALUES(:symbol, :shares, :price, :id)", \
                        shares=-shares, price=usd(sell_stock["price"]), \
                        symbol=sell_stock["symbol"], id=session["user_id"])


        if user_shares[0]["Shares"] - shares==0:
            db.execute("DELETE FROM portfolio \
                        WHERE id=:id AND Symbol=:symbol", \
                        id=session["user_id"], \
                        symbol=sell_stock["symbol"])
        else:
            db.execute("UPDATE portfolio SET Shares=:shares \
                    WHERE id=:id AND Symbol=:symbol", \
                    shares=user_shares[0]["Shares"] - shares, id=session["user_id"], \
                    symbol=sell_stock["symbol"])

        return redirect(url_for("index"))

    else:
        return render_template("sell.html")

    return apology("Error")


@app.route("/add_cash", methods=["GET", "POST"])
@login_required
def add_cash():
    """Add cash to account."""
    if request.method=="POST":
        #Did they enter cash
        if not request.form.get("added_cash"):
            return apology("Please enter the amount of cash you wish to add to your account")

    if not request.form.get("added_cash").isnumeric():
            return apology("Please enter an integer value")

        #Did they enter a positive amount
    if int(request.form.get("added_cash"))<=0:
        return apology("Please enter a positive amount")


        old_cash= db.execute("SELECT cash FROM users \
                               WHERE id=:id", id=session["user_id"])

        #Find their money
        if not old_cash:
            return apology("Error obtaining money from your account")


        db.execute("UPDATE users SET cash = cash + :added_cash WHERE id = :id", id=session["user_id"], \
                    added_cash=int(request.form.get("added_cash")))

        return redirect(url_for("index"))

    else:
        return render_template("add_cash.html")

