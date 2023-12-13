from flask import Flask, render_template

app = Flask(__name__)


@app.route("/members")
def members():
    members = ["Bob", "Tom", "Ken"]
    return render_template("members.html", members=members)

if __name__ == "__main__":
    app.run(port=8000, debug=True)
