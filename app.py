from flask import Flask, render_template

app = Flask(__name__)

@app.route("/<page1>", methods=["GET"])
def page(page1):
    return render_template("home.html", name=page1)

if __name__ == "__main__":
    app.run(host="localhost", port=5050)