from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/estimate", methods=["POST"])
def estimate():
    url = request.form["url"]

    # Dummy calculation (for now)
    # Later we can replace this with real logic
    estimated_revenue = "$" + str(len(url) * 10)  # just a fake formula

    return render_template("result.html", url=url, revenue=estimated_revenue)

if __name__ == "__main__":
    app.run(debug=True)
