from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key = "secret123"

# MySQL Configuration
app.config["MYSQL_HOST"] = "mysql"      # Use "localhost" if not using Docker
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "amar"
app.config["MYSQL_DB"] = "flaskapp"

mysql = MySQL(app)


@app.route("/", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form["email"]
        password = request.form["password"]

        cur = mysql.connection.cursor()
        cur.execute(
            "SELECT * FROM users WHERE email=%s AND password=%s",
            (email, password)
        )

        user = cur.fetchone()
        cur.close()

        if user:
            return render_template("dashboard.html", user=user)
        else:
            flash("Invalid Email or Password")

    return render_template("login.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)