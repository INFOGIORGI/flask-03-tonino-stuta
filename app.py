from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")
@app.route("/details")
def details():
    cristiani = (("Daniel", "Calabrese", 18, "Volkswagen UP!"), ("Antonio", "Iaia", 18, "Citroen C3"), ("Angelo", "Basile", 18, "Opel Corsa") )
    return render_template("details.html", cristiani = cristiani)
app.run(debug="true")
